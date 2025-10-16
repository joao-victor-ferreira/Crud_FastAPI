from fastapi import APIRouter
from app.schemas.user_schemas import UserCreate, UserUpdate, UserOut
from app.services.user_services import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)
from app.exceptions.user_exceptions import UserNotFound, UserAlreadyExists

router = APIRouter()

@router.get("/users", response_model=list[UserOut], summary="Lista todos os usuários")
async def list_users():
    return await get_all_users()

@router.get("/users/{user_id}", response_model=UserOut, summary="Obter usuário pelo ID")
async def get_user(user_id: str):
    return await get_user_by_id(user_id)

@router.post("/users", response_model=UserOut, summary="Criar novo usuário")
async def create_user_route(user: UserCreate):
    return await create_user(user)

@router.put("/users/{user_id}", response_model=UserOut, summary="Atualizar usuário")
async def update_user_route(user_id: str, user: UserUpdate):
    return await update_user(user_id, user)

@router.delete("/users/{user_id}", response_model=UserOut, summary="Deletar usuário")
async def delete_user_route(user_id: str):
    return await delete_user(user_id)
