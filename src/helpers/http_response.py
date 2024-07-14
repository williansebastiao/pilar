import json
from fastapi.responses import JSONResponse

from src.helpers.enums import StatusCode


class HttpResponse:

    def __init__(self, status_code: int = StatusCode.OK, content: dict = []):
        self.status_code = status_code
        self.content = content

    def json(self):
        return JSONResponse(status_code=self.status_code.value, content=self.content)
