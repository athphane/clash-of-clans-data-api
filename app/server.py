from fastapi import FastAPI, HTTPException, status, Request
from fastapi.openapi.models import Server
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi.middleware.cors import CORSMiddleware

from app.routers.army_buildings import army_buildings_router
from app.routers.traps import traps_router


app = FastAPI(
    servers=[
        {"url": "https://coc-data.athfan.dev", "description": "Development Server"},
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

app.include_router(army_buildings_router)


@app.get("/")
def index(request: Request):
    return {"Hello": "World"}

