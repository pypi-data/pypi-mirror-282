from __future__ import annotations

import asyncio
import logging
import sys
from typing import Any, Dict, Optional, Union

import aiohttp

from artfight import __version__, error
from artfight.util import Method

_log = logging.getLogger(__name__)

RETRY_ATTEMPTS = 5
SESSION_COOKIE = "laravel_session"
BASE_URL = "https://artfight.net/"


def join_url(base: str, route: str) -> str:
    """Joins two urls ensuring there is only one slash in between them.

    Parameters
    ----------
    base : str
        The base url to join to.
    route : str
        The route to join to the base url.

    Returns
    -------
    str
        The merged url.
    """
    if base.endswith("/"):
        base = base[:-1]
    if route.startswith("/"):
        route = route[1:]
    return base + "/" + route


class HTTPClient:
    """HTTPClient handles all the HTTP requests performed by artfight-api

    Parameters
        ----------
        username : str
            The username to log in with.
        password : str
            The password to log in with.
    """

    def __init__(self, username: str, password: str) -> None:
        user_agent = "Artfight Bot (https://github.com/NimajnebEC/artfight-api v{0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
        self.user_agent: str = user_agent.format(__version__, sys.version_info, aiohttp.__version__)
        self._client: Union[aiohttp.ClientSession, None] = None
        self._session: Union[str, None] = None
        self._username: str = username
        self._password: str = password

    async def __aenter__(self) -> HTTPClient:
        return self

    async def __aexit__(self, *_) -> None:
        await self.close()

    async def close(self):
        """Closes the HTTP connection if it exists."""
        if self._client is not None:
            await self._client.close()

    async def request(
        self,
        method: Method,
        url: str,
        *,
        form: Optional[Dict[str, Any]] = None,
        authenticated: bool = True,
    ) -> str:
        """Wraps aiohttp requests

        Parameters
        ----------
        route : Route
            The route data to perform the request against
        form : Dict[str, Any], optional
            If specified, the form data to include in the body of the request., by default None.
        authenticated : bool, optional
            Wether the client should be authenticated to perform this request, by default True.

        Returns
        -------
        str
            The HTML returned by the request or the redirect destination.

        Raises
        ------
        NotAuthenticated
            Raised when an authenticated request is attempted before the client has logged in.
        UnauthorizedError
            Raised when trying to access a protected route when not logged in.
        NotFoundError
            Raised when the server replies with 404.
        ArtfightServerError
            Raised when an error occurs on the artfight servers.
        HTTPResponseError
            Raised when an arbitrary response it recieved.
        RuntimeError
            Raised when the HTTP connection has not been initialised.
        """
        url = join_url(BASE_URL, url)
        data = None

        # ensure client is set up
        if self._client is None:
            self._client = aiohttp.ClientSession()

        # initialise headers
        headers: dict[str, str] = {
            "User-Agent": self.user_agent,
        }

        # add session cookie
        if self._session is None:
            if authenticated:
                _log.debug("Session not found; logging in...")
                await self.login()
        else:
            headers["Cookie"] = f"{SESSION_COOKIE}={self._session}"

        # add form data if applicable
        if form is not None:
            data = aiohttp.FormData(form)

        response = None
        for tries in range(RETRY_ATTEMPTS):
            await asyncio.sleep(tries * 2)

            try:
                async with self._client.request(
                    allow_redirects=False,
                    method=method,
                    headers=headers,
                    data=data,
                    url=url,
                ) as response:
                    _log.debug("%s %s : %s", method, url, response.status)

                    # update session
                    token = response.cookies.get(SESSION_COOKIE)
                    if token is not None:
                        self._session = token.value

                    # successful request
                    if 300 > response.status >= 200:
                        return await response.text()

                    # redirected
                    if response.status == 302:
                        # check redirected to login (unauthorized)
                        location = response.headers.get("Location")
                        if location is not None:
                            if location.endswith("/login"):
                                # login and try again
                                if authenticated:
                                    _log.debug("Unauthorized response recieved; logging in and trying again...")
                                    await self.login()
                                    tries -= 0
                                    continue
                                raise error.UnauthorizedError(method, url)
                            return location

                    # unconditional retry
                    if response.status in (500, 502, 504, 524):
                        continue

                    # special errors
                    elif response.status == 404:
                        raise error.NotFoundError(method, url)
                    elif response.status >= 500:
                        raise error.ArtfightServerError(method, url, response.status)
                    else:
                        raise error.HTTPResponseError(method, url, response.status)

            except OSError as e:
                # connection reset
                if e.errno in (54, 10054):
                    continue
                raise

        if response is not None:
            # We've run out of retries, raise.
            if response.status >= 500:
                raise error.ArtfightServerError(method, url, response.status)
            raise error.HTTPResponseError(method, url, response.status)

        raise RuntimeError("_RETRY_ATTEMPTS was < 1")

    async def login(self) -> None:
        """Login to the artfight servers using the specified credentials

        Raises
        ------
        LoginError
            Raised when the provided credentials are invalid
        """
        try:
            await self.request(
                "POST",
                "/login",
                authenticated=False,
                form={"username": self._username, "password": self._password},
            )
        except error.UnauthorizedError:
            raise error.LoginError()
