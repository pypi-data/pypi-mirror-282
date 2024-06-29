import jwt
from fastapi import FastAPI, Request, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from typing import List, Type
from beanie import Document


class JWTMiddleware:
    def __init__(self, app: FastAPI, secret_key: str, algorithm: str):
        self.app = app
        self.secret_key = secret_key
        self.algorithm = algorithm

    async def __call__(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if token:
            try:
                token = token.split(" ")[1]
                payload = jwt.decode(
                    token, self.secret_key, algorithms=[self.algorithm]
                )
                username = payload.get("sub")
                if username:
                    request.state.username = username
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
                    )
            except jwt.PyJWTError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
                )
        response = await call_next(request)
        return response

@asynccontextmanager
async def lifespan(app: FastAPI, database_url: str, document_models: List[Type[Document]]):
    client = AsyncIOMotorClient(database_url)
    database = client.get_default_database()
    await init_beanie(database, document_models=document_models)
    yield
    client.close()
