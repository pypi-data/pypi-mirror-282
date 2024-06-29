from dataclasses import dataclass
from typing import Optional, Dict, List
from datetime import datetime
from packaging.version import Version

from e2b.api import ApiClient, models, client, exceptions
from e2b.connection_config import ConnectionConfig
from e2b.api import handle_api_exception


class E2BUpdateTemplateException(Exception):
    """
    Exception raised when the template uses old envd version. It isn't compatible with the new SDK.
    """


@dataclass
class SandboxInfo:
    """Information about a sandbox."""

    sandbox_id: str
    """Sandbox ID."""
    template_id: str
    """Template ID."""
    name: Optional[str]
    """Sandbox name."""
    metadata: Optional[Dict[str, str]]
    """Saved sandbox metadata."""
    started_at: datetime
    """Sandbox start time."""


class SandboxApi:
    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        debug: Optional[bool] = None,
        request_timeout: Optional[float] = None,
    ) -> List[SandboxInfo]:
        config = ConnectionConfig(
            api_key=api_key,
            domain=domain,
            debug=debug,
            request_timeout=request_timeout,
        )

        with ApiClient(config) as api_client:
            try:
                return [
                    SandboxInfo(
                        sandbox_id=SandboxApi._get_sandbox_id(
                            sandbox.sandbox_id,
                            sandbox.client_id,
                        ),
                        template_id=sandbox.template_id,
                        name=sandbox.alias,
                        metadata=sandbox.metadata,
                        started_at=sandbox.started_at,
                    )
                    for sandbox in client.SandboxesApi(api_client).sandboxes_get(
                        _request_timeout=config.request_timeout,
                    )
                ]
            except exceptions.ApiException as e:
                raise handle_api_exception(e)

    @classmethod
    def _cls_kill(
        cls,
        sandbox_id: str,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        debug: Optional[bool] = None,
        request_timeout: Optional[float] = None,
    ) -> None:
        config = ConnectionConfig(
            api_key=api_key,
            domain=domain,
            debug=debug,
            request_timeout=request_timeout,
        )

        with ApiClient(config) as api_client:
            try:
                client.SandboxesApi(api_client).sandboxes_sandbox_id_delete(
                    sandbox_id,
                    _request_timeout=config.request_timeout,
                )
            except exceptions.ApiException as e:
                raise handle_api_exception(e)

    @classmethod
    def _cls_set_timeout(
        cls,
        sandbox_id: str,
        timeout: int,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        debug: Optional[bool] = None,
        request_timeout: Optional[float] = None,
    ) -> None:
        config = ConnectionConfig(
            api_key=api_key,
            domain=domain,
            debug=debug,
            request_timeout=request_timeout,
        )

        with ApiClient(config) as api_client:
            try:
                client.SandboxesApi(api_client).sandboxes_sandbox_id_timeout_post(
                    sandbox_id,
                    models.SandboxesSandboxIDTimeoutPostRequest(timeout=timeout),
                    _request_timeout=config.request_timeout,
                )
            except exceptions.ApiException as e:
                raise handle_api_exception(e)

    @classmethod
    def _create_sandbox(
        cls,
        template: str,
        metadata: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        debug: Optional[bool] = None,
        request_timeout: Optional[float] = None,
    ) -> str:
        config = ConnectionConfig(
            api_key=api_key,
            domain=domain,
            debug=debug,
            request_timeout=request_timeout,
        )

        with ApiClient(config) as api_client:
            try:
                res = client.SandboxesApi(api_client).sandboxes_post(
                    models.NewSandbox(
                        templateID=template,
                        metadata=metadata,
                        timeout=timeout,
                    ),
                    _request_timeout=config.request_timeout,
                )
                if Version(res.envd_version) < Version("0.1.0"):
                    raise E2BUpdateTemplateException(
                        "You need to update the template to use the new SDK. "
                        "You can do this by running `e2b template build` in the directory with the template."
                    )
                return SandboxApi._get_sandbox_id(res.sandbox_id, res.client_id)
            except exceptions.ApiException as e:
                raise handle_api_exception(e)

    @staticmethod
    def _get_sandbox_id(sandbox_id: str, client_id: str) -> str:
        return f"{sandbox_id}-{client_id}"
