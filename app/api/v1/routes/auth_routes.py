from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from jose import JWTError, jwt
from app.db.models.user_model import User
from app.services.auth_services import authenticate_user
from app.core.security import SECRET_KEY, ALGORITHM
from beanie import PydanticObjectId

router = APIRouter()

# Modelo de entrada para login
class LoginRequest(BaseModel):
    email: str
    password: str

# Modelo de saída
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# -------------------- LOGIN --------------------
@router.post("/auth/login", response_model=TokenResponse, summary="Autentica o usuário e retorna o token JWT")
async def login(request: LoginRequest):
    return await authenticate_user(request.email, request.password)

# -------------------- ROTA PROTEGIDA /me --------------------
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        return user_id
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

@router.get("/auth/me", summary="Retorna o usuário autenticado")
async def get_current_user(token: str):
    user_id = decode_token(token)
    user = await User.get(PydanticObjectId(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {
        "id": str(user.id),
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    }
