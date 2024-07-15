from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.helpers.enums import StatusCode
from src.helpers.http_response import HttpResponse
from src.schemas.words_schema import SortSchema, VowelCountSchema
from src.services.word_services import WordServices

router = APIRouter(prefix="/api")


@router.get("/", tags=["Health check"])
async def index() -> JSONResponse:
    content = {"detail": "It's running :)"}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post("/words/vowel_count", tags=["Words"])
async def vowel_count(body: VowelCountSchema) -> JSONResponse:
    services = WordServices()
    content = services.vowel_count(body.words)
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post("/words/sort", tags=["Words"])
async def order_words(body: SortSchema) -> JSONResponse:
    services = WordServices()
    content = services.sort(body)
    return HttpResponse(status_code=StatusCode.OK, content=content).json()
