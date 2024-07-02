from __future__ import annotations

from typing import Optional


class APIExceptionError(Exception):
    def __init__(
        self,
        error_code: Optional[str],
        message: Optional[str],
    ) -> None:
        super().__init__(message)
        self.error_code = error_code or "unknown"
        self.message = message or "unknown"

    def __str__(self) -> str:
        return f"APIExceptionError(status_code={self.error_code}, message={self.message})"

    def __repr__(self) -> str:
        return self.__str__()
