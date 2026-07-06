from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.upload import router as upload_router

from app.core.config import settings
from app.core.middleware import LoggingMiddleware
from app.core.exceptions import global_exception_handler
from app.core.startup import startup


@asynccontextmanager
async def lifespan(app: FastAPI):

    startup()

    yield

    print("Application shutting down...")


app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION,

    lifespan=lifespan

)

app.add_middleware(
    LoggingMiddleware
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(chat_router)

app.include_router(upload_router)


@app.get("/")
def root():

    return {

        "application": settings.APP_NAME,

        "version": settings.APP_VERSION,

        "status": "healthy"

    }


@app.get("/health")
def health():

    return {

        "status": "UP"

    }