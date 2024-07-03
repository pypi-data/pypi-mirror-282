from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions import MicroserviceException


def add_domain_exception_middleware(app: FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except MicroserviceException as e:
            return JSONResponse(content={
                'error': e.message
            }, headers={'Content-Type': 'application/problem+json'}, status_code=200)
        except Exception:
            raise
