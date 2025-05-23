from fastapi import FastAPI, HTTPException, Response, status, Request
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware

from app.routers import traps_router

app = FastAPI()
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

app.include_router(traps_router)

@app.get("/")
def index(request: Request):
    return {"Hello": "World"}

@app.get("/admin")
def admin():
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="I'm a teapot"
    )