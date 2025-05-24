from fastapi import FastAPI, HTTPException, status, Request
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi.middleware.cors import CORSMiddleware

from app.routers.barracks import barracks_router
from app.routers.traps import traps_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

app.include_router(traps_router)
app.include_router(barracks_router)


@app.get("/")
def index(request: Request):
    return {"Hello": "World"}


@app.get("/admin")
def admin():
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="I'm a teapot"
    )
