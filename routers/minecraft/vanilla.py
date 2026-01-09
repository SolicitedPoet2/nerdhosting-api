from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..websocket import websockets
from ...utils.logger import logger
from ..websocket import websockets, isConnected
from typing import Final, Optional
import secrets

router = APIRouter(
    prefix="/vanilla",
    tags=["vanilla"],
    responses={404: {"message":"This request was invalid"}},
)

"""
Data Structure JSON
    id: str # Unique ID upon creating the server from the website
    name: str # Server Name
    version: str # Minecraft Version
    voicechat: bool # Voice Chat Support?
    GPU: bool # GPU Accelerated?
    ram: int # In Gigabytes
    cpu: int # Cores
"""


class PostVanilla(BaseModel): # Responsible by creating Vanilla Servers
    id: Final[str] = secrets.token_urlsafe(8).lower()
    name: str 
    version: str
    voicechat: bool
    GPU: bool
    ram: int
    cpu: int 

class GetVanilla(BaseModel): # Responsible by getting a list of servers or searching for a specific Vanilla Server
    id: Optional[str]

class DeleteVanilla(BaseModel): # Responsible deleting a specific Vanilla Server
    id: str

class PutVanilla(BaseModel): # Responsible for changing Vanilla Server plans and version
    id: str
    name: str
    version: str
    voicechat: bool
    GPU: bool 
    ram: int 
    cpu: int

@router.post("/create", status_code=201)
async def vanilla(vanilla: PostVanilla, status_code=201):
    pass

@router.get("/list", status_code=201)
async def vanilla(vanilla: GetVanilla, status_code=201):
    pass

@router.post("/delete", status_code=201)
async def vanilla(vanilla: DeleteVanilla, status_code=201):
    pass

@router.put("/update", status_code=201)
async def vanilla(vanilla: PutVanilla, status_code=201):
    pass