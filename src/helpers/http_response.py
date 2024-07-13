import json
from fastapi import Response

from src.helpers.status_code import StatusCode


class HttpResponse:

    def __init__(self, status_code: int = StatusCode.OK, content: dict = None):
        self.status_code = status_code
        self.content = content

    def json(self):
        return Response(status_code=self.status_code.value, content=json.dumps(self.content),
                        headers={"Content-Type": "application/json"})
