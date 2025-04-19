import requests
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi import Request
from starlette.responses import JSONResponse

from api.routes import nutrition

app = FastAPI()


#  Global exception handler to show real status code
@app.exception_handler(requests.exceptions.HTTPError)
async def http_error_handler(request: Request, exc: requests.exceptions.HTTPError):
    status_code = exc.response.status_code
    return JSONResponse(
        status_code=status_code,
        content={
            "error": str(exc)
        }
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nutrition.router, tags=["nutrition"])
