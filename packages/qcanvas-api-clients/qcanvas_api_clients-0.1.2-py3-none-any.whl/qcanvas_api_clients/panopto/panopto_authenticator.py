import logging

from qcanvas_api_clients.canvas.canvas_client import CanvasClient
from qcanvas_api_clients.panopto.panopto_api_config import PanoptoApiConfig
from qcanvas_api_clients.util.authenticator import Authenticator


class PanoptoAuthenticator(Authenticator):
    _logger = logging.getLogger(__name__)

    def __init__(
        self, panopto_api_config: PanoptoApiConfig, canvas_client: CanvasClient
    ):
        super().__init__(canvas_client._client)
        self._panopto_api_config = panopto_api_config
        self._canvas_client = canvas_client

    async def _authenticate(self) -> None:
        self._logger.debug("Authenticating to panopto")

        response = await self._canvas_client.authenticate_panopto(
            self._panopto_api_config.get_endpoint(
                "Panopto/Pages/Auth/Login.aspx?instance=Canvas&AllowBounce=true"
            )
        )

        response.raise_for_status()
        self._logger.debug("Authentication complete")
