from typing import Optional, List
from datetime import datetime

class ErrorResponse:
    def __init__(self,
                code: Optional[str] = None,
                message: Optional[str] = None,
                details: Optional[List[str]] = None,
                timestamp: Optional[datetime] = None):
        self._code = code
        self._message = message
        self._details = details if details is not None else []
        self._timestamp = timestamp if timestamp is not None else datetime.now()

    # Getters and Setters
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

class ErrorResponseBuilder:
    def __init__(self):
        self._code: Optional[str] = None
        self._message: Optional[str] = None
        self._details: Optional[List[str]] = None
        self._timestamp: Optional[datetime] = None

    def code(self, code: str) -> 'ErrorResponseBuilder':
        self._code= code
        return self

    def message(self, message: str) -> 'ErrorResponseBuilder':
        self._message= message
        return self

    def details(self, details: str) -> 'ErrorResponseBuilder':
        self._details= details
        return self

    def timestamp(self, timestamp: str) -> 'ErrorResponseBuilder':
        self._timestamp= timestamp
        return self

    def build(self) -> ErrorResponse:
        return ErrorResponse(self._code,
                            self._message,
                            self._details,
                            self._timestamp)

# error_response = (ErrorResponseBuilder()
#                   .code("ERR001")
#                   .message("Invalid request")
#                   .details(["Missing 'name' field", "Invalid 'age' value"])
#                   .timestamp(datetime.now())
#                   .build())