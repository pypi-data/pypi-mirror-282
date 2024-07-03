from httpx import Response

from qcanvas_api_clients.util.authenticator import (
    AUTHENTICATION_REQUIRED_RESPONSE_CODE,
)


class PanoptoUnauthenticatedDetectorHook:
    def __init__(self, panopto_host: str):
        self.panopto_host = panopto_host

    async def __call__(self, *args, **kwargs) -> None:
        response: Response = args[0]

        assert isinstance(response, Response)

        if response.url.host != self.panopto_host:
            return

        auth_cookie = ".ASPXAUTH"
        if not response.is_server_error and not response.is_redirect:
            if (
                auth_cookie not in response.cookies.keys()
                or response.cookies.get(auth_cookie) == ""
            ):
                response.status_code = AUTHENTICATION_REQUIRED_RESPONSE_CODE
