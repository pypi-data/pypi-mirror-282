from typing import Any, Callable, Protocol, TypeAlias

# Define type aliases for JSON serialization and deserialization functions
JsonLoads: TypeAlias = Callable[[str], Any]
JsonDumps: TypeAlias = Callable[[Any], str]


class SessionProto(Protocol):
    """
    Protocol defining the interface for an asynchronous session.

    Properties:
        closed (bool): Indicates if the session is closed.

    Methods:
        close() -> None:
            Close the session.

        request(method: str, endpoint: str, **kwargs: Any) -> dict[str, Any]:
            Make an HTTP request with the specified method and endpoint.

        get(endpoint: str, params: dict[str, Any] | None = None, **kwargs: Any) -> dict[str, Any]:
            Make a GET request to the specified endpoint with optional parameters.

        post(endpoint: str, data: dict[str, Any] | None = None, **kwargs: Any) -> dict[str, Any]:
            Make a POST request to the specified endpoint with optional data.

        delete(endpoint: str, **kwargs: Any) -> dict[str, Any]:
            Make a DELETE request to the specified endpoint.
    """

    @property
    def closed(self) -> bool:
        """
        Check if the session is closed.

        Returns:
            bool: True if the session is closed, False otherwise.
        """
        raise NotImplementedError

    async def close(self) -> None:
        """
        Close the session.

        Returns:
            None
        """
        raise NotImplementedError

    async def request(
        self, method: str, endpoint: str, **kwargs: Any
    ) -> Any:
        """
        Make an HTTP request with the specified method and endpoint.

        Args:
            method (str): The HTTP method to use (e.g., 'GET', 'POST').
            endpoint (str): The endpoint URL to make the request to.
            **kwargs (Any): Additional arguments to pass to the request.

        Returns:
            Any: The JSON response
        """
        raise NotImplementedError

    async def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Any:
        """
        Make a GET request to the specified endpoint with optional parameters.

        Args:
            endpoint (str): The endpoint URL to make the GET request to.
            params (dict[str, Any] | None): Optional parameters to include in the request.
            **kwargs (Any): Additional arguments to pass to the request.

        Returns:
            Any: The JSON response
        """
        raise NotImplementedError

    async def post(
        self, endpoint: str, data: dict[str, Any] | None = None, **kwargs: Any
    ) -> Any:
        """
        Make a POST request to the specified endpoint with optional data.

        Args:
            endpoint (str): The endpoint URL to make the POST request to.
            data (dict[str, Any] | None): Optional data to include in the request body.
            **kwargs (Any): Additional arguments to pass to the request.

        Returns:
            Any: The JSON response
        """
        raise NotImplementedError

    async def delete(self, endpoint: str, **kwargs: Any) -> Any:
        """
        Make a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The endpoint URL to make the DELETE request to.
            **kwargs (Any): Additional arguments to pass to the request.

        Returns:
            Any: The JSON response
        """
        raise NotImplementedError
