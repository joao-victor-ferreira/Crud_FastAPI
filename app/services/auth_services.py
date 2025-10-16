from datetime import timedelta
from app.db.models.user_model import User
from app.core.security import verify_password, create_access_token
from app.exceptions.user_exceptions import UserNotFound
from app.core.logger import logger

async def authenticate_user(email: str, password: str):
    user = await User.find_one(User.email == email)
    if not user or not verify_password(password, user.password):
        logger.warning(f"Tentativa de login inválida: {email}")
        raise UserNotFound("Credenciais inválidas")
    
    token_expires = timedelta(minutes=60)
    access_token = create_access_token({"sub": str(user.id)}, token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
