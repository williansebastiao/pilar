from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.helpers.http_response import HttpResponse
from src.helpers.status_code import StatusCode
from src.schemas.vowel_count_schema import VowelCountSchema
from src.schemas.sort_schema import SortSchema
from src.services.vowel_count_services import VowelCountServices

router = APIRouter(prefix="/api")


@router.get('/', tags=['Health Check'])
async def index() -> JSONResponse:
    content = {'message': "It's running..."}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post('/vowel_count', tags=['Counts vowels in words'])
async def vowel_count(body: VowelCountSchema) -> JSONResponse:
    vowel_count_services = VowelCountServices()
    content = vowel_count_services.vowel_count(body.words)
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post('/sort', tags=['Order words'])
async def order_words(body: SortSchema) -> JSONResponse:
    content = {'message': 'Order words'}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()
