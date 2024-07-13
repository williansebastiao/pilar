from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from src.helpers.http_response import HttpResponse
from src.helpers.status_code import StatusCode


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    content = {"message": errors[0]['msg']}
    return HttpResponse(status_code=StatusCode.UNPROCESSABLE_ENTITY, content=content).json()
