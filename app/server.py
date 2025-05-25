from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from app import FAST_API_RELOAD
from app.routers.army_buildings import army_buildings_router
from app.routers.traps import traps_router

if FAST_API_RELOAD:
    servers = [
        {"url": "http://localhost:8001", "description": "Development Server"},
    ]
else:
    servers = [
        {"url": "https://coc-data.athfan.dev", "description": "Production Server"},
    ]

app = FastAPI(
    title='Clash of Clans Data API',
    summary='An API to provide Clash of Clans data scarped from the official wiki',
    version='0.1',
    servers=servers
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
app.include_router(traps_router)

@app.get("/")
def index(request: Request):
    return {"Hello": "World"}
