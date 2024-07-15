from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.helpers.enums import StatusCode
from src.helpers.http_response import HttpResponse

router = APIRouter()


@router.get("/", tags=["Default"])
async def index() -> JSONResponse:
    content = {"detail": "It's running"}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()
