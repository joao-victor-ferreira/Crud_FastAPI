# tests/test_users.py
import pytest
from app.schemas.user_schemas import UserCreate

@pytest.mark.asyncio
async def test_create_user(async_client):
    payload = {
        "name": "Joao Silva",
        "phone": "11999999999",
        "email": "joao.silva1@test.com",
        "password": "123456"
    }

    response = await async_client.post("/api/v1/users", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == payload["email"]

@pytest.mark.asyncio
async def test_get_user_by_id(async_client):
    # Primeiro cria o usuário
    create_payload = {
        "name": "Joao Silva",
        "phone": "11999999999",
        "email": "joao.silva2@test.com",
        "password": "123456"
    }
    create_resp = await async_client.post("/api/v1/users", json=create_payload)
    user_id = create_resp.json()["id"]

    # Agora busca
    response = await async_client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

@pytest.mark.asyncio
async def test_update_user(async_client):
    # Criar usuário
    create_payload = {
        "name": "Joao Silva",
        "phone": "11999999999",
        "email": "joao.silva3@test.com",
        "password": "123456"
    }
    create_resp = await async_client.post("/api/v1/users", json=create_payload)
    user_id = create_resp.json()["id"]

    update_payload = {
        "name": "Joao Atualizado",
        "phone": "11988888888"
    }
    response = await async_client.put(f"/api/v1/users/{user_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_payload["name"]

@pytest.mark.asyncio
async def test_delete_user(async_client):
    # Criar usuário
    create_payload = {
        "name": "Joao Silva",
        "phone": "11999999999",
        "email": "joao.silva4@test.com",
        "password": "123456"
    }
    create_resp = await async_client.post("/api/v1/users", json=create_payload)
    user_id = create_resp.json()["id"]

    # Deletar
    response = await async_client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
