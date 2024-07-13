from fastapi import APIRouter, Response

from src.helpers.http_response import HttpResponse
from src.helpers.status_code import StatusCode
from src.schemas.vowel_count_schema import VowelCountSchema
from src.schemas.sort_schema import SortSchema

router = APIRouter(prefix="/api")


@router.get('/', tags=['Health Check'])
async def index() -> Response:
    content = {'message': "It's running..."}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post('/vowel_count', tags=['Counts vowels in words'])
async def vowel_count(body: VowelCountSchema) -> Response:
    print(body.words)
    content = {'message': 'Counts vowels in words'}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post('/sort', tags=['Order words'])
async def order_words(body: SortSchema) -> Response:
    content = {'message': 'Order words'}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()
