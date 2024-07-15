from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.helpers.enums import StatusCode
from src.helpers.http_response import HttpResponse
from src.routes.api import router as api_router
from src.routes.web import router as web_router

app = FastAPI(title="Pilar")

app.include_router(web_router)
app.include_router(api_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    errors = exc.errors()
    content = {"detail": errors[0]["msg"]}
    return HttpResponse(
        status_code=StatusCode.UNPROCESSABLE_ENTITY, content=content
    ).json()
