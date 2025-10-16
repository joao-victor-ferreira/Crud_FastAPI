# tests/conftest.py
import pytest_asyncio
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from app.main import app

@pytest_asyncio.fixture
async def async_client():
    async with LifespanManager(app):  # gerencia startup/shutdown events
        async with AsyncClient(app=app, base_url="http://test") as client:
            yield client
