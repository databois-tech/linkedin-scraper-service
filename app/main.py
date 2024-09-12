from fastapi import FastAPI, Request
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from .exception.invalid_request_exception import InvalidRequestException

#import asyncio

from .route import user_posts

app = FastAPI(title='DottyPostHq', description='Linkedin Scraper micro services', version='0.1', docs_url="/documentation", redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Or specify the allowed methods, e.g., ["GET", "POST"]
    allow_headers=["*"],  # Or specify the allowed headers
)
@app.get("/fetch-info")
def root():
    return {"service": "Dotty scraper micro service",
            "version": "0.1"}

app.include_router(user_posts.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": {
            "name": "error",
            "message": "Invalid input data",
            "status": 422,
            "reason": "VALIDATION_ERROR",
            "type": "Bad Request",
            "statusCode": "422"
        }},
    )


@app.exception_handler(InvalidRequestException)
async def custom_http_exception_handler(request, exc):
    response_content = {
        "error": {
            "name": "error",
            "message": exc.detail,
            "status": exc.status_code,
            "reason": "VALIDATION_ERROR",
            "type": "Bad Request",
            "statusCode": str(exc.status_code),
        }
    }
    return JSONResponse(content=response_content, status_code=exc.status_code)