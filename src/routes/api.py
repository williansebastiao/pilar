from fastapi import APIRouter, Response

from src.helpers.http_response import HttpResponse
from src.helpers.status_code import StatusCode

router = APIRouter(prefix="/api")


@router.get('/', tags=['Health Check'])
async def index() -> Response:
    content = {'message': 'Hello World'}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post('/vowel_count', tags=['Counts vowels in words'])
async def vowel_count() -> Response:
    content = {'message': 'Counts vowels in words'}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()


@router.post('/sort', tags=['Order words'])
async def order_words() -> Response:
    content = {'message': 'Order words'}
    return HttpResponse(status_code=StatusCode.OK, content=content).json()
