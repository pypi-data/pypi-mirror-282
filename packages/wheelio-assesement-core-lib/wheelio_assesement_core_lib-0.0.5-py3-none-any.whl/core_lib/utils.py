from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient

def get_current_username(request: Request):
    return request.session.get("user")

async def get_mongo_db(DATABASE_URL: str):
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client.get_default_database()
    try:
        yield db
    finally:
        client.close()
