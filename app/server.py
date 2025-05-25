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


@app.get('/openai.json')
def open_ai_tool_json():
    return {
        "openapi": "3.1.0",
        "info": {
            "title": "Clash of Clans Data API",
            "description": "An API that provides data about Clash of Clans, including troops, buildings, and traps and more.",
            "version": "v1.0.0"
        },
        "servers": [
            {
            "url": "https://clash-of-clans-data-api.athfan.dev"
            }
        ],
        "paths": {
            "/barracks/troop_all_info": {
                "get": {
                    "description": "Get all information about a troop in CSV format. The name of the troop should be written properly as a noun, e.g., 'Barbarian' or 'Archer'.",   
                    "operationId": "GetTroopInfoAll",
                    "parameters": [
                        {
                            "name": "troop_name",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "deprecated": False
                }
            },
            "/barracks/troops": {
                "get": {
                    "description": "Get list of all troops available in Clash of Clans.",   
                    "operationId": "ListAllTroops",
                    "parameters": [],
                    "deprecated": False
                }
            },
            "/spells/spells_all_info": {
                "get": {
                    "description": "Get all the information about a spell in CSV format. The name of the spell should be written properly as a noun, e.g., 'Lightning Spell' or 'Healing Spell'.",   
                    "operationId": "GetSpellAllInfo",
                    "parameters": [
                        {
                            "name": "spell_name",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "deprecated": False
                }
            },
        },
        "components": {
            "schemas": {}
        }
}

@app.get("/admin")
def admin():
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="I'm a teapot"
    )
