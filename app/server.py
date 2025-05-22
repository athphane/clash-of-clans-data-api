from fastapi import FastAPI, HTTPException, Response, status

from app.routers import traps_router

app = FastAPI()


app.include_router(traps_router)

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/admin")
def admin():
    raise HTTPException(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        detail="I'm a teapot"
    )