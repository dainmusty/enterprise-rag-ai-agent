import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        request_id = str(uuid.uuid4())[:8]

        start = time.perf_counter()

        logger.info(
            f"[{request_id}] {request.method} {request.url.path}"
        )

        response = await call_next(request)

        elapsed = round(
            time.perf_counter() - start,
            3
        )

        logger.info(
            f"[{request_id}] {response.status_code} ({elapsed}s)"
        )

        response.headers["X-Request-ID"] = request_id

        return response