import jwt
import os
from typing import Callable
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

class JWTMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, secret_key: str, algorithm: str):
        super().__init__(app)
        self.secret_key = secret_key
        self.algorithm = algorithm

    async def dispatch(self, request: Request, call_next):
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

#TODO: Modify this to accept a DATABASE_URL
async def get_mongo_db(DATABASE_URL: str):
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client.get_default_database()
    try:
        yield db
    finally:
        client.close()
