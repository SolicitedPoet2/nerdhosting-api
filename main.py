from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from .dependencies import get_query_token
from .routers import websocket
from .utils import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_db_and_tables()
    yield
     
app = FastAPI(dependencies=[Depends(get_query_token)], lifespan=lifespan)
app.include_router(websocket.router)

@app.get("/")
async def root():
    return {"message": "Ayo!"}