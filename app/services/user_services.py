from app.db.models.user_model import User
from app.schemas.user_schemas import UserCreate, UserUpdate, UserOut
from app.core.security import hash_password
from app.exceptions.user_exceptions import UserAlreadyExists, UserNotFound
from app.core.logger import logger

# ---------- CREATE ----------
async def create_user(user_create: UserCreate) -> UserOut:
    existing_user = await User.find_one(User.email == user_create.email)
    if existing_user:
        logger.warning(f"Tentativa de criar usuário com e-mail existente: {user_create.email}")
        raise UserAlreadyExists()

    hashed_pwd = hash_password(user_create.password)

    user = User(
        name=user_create.name,
        phone=user_create.phone,
        email=user_create.email,
        password=hashed_pwd,
    )

    await user.insert()
    logger.info(f"Usuário criado com sucesso: {user.email}")

    return UserOut(**user.dict())

# ---------- READ ----------
async def get_all_users() -> list[UserOut]:
    users = await User.find_all().to_list()
    return [UserOut(**u.dict()) for u in users]

async def get_user_by_id(user_id: str) -> UserOut:
    user = await User.get(user_id)
    if not user:
        logger.error(f"Usuário não encontrado: {user_id}")
        raise UserNotFound()
    return UserOut(**user.dict())

# ---------- UPDATE ----------
async def update_user(user_id: str, user_update: UserUpdate) -> UserOut:
    user = await User.get(user_id)
    if not user:
        raise UserNotFound()

    update_data = user_update.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    await user.set(update_data)
    logger.info(f"Usuário atualizado: {user_id}")

    return UserOut(**user.dict())

# ---------- DELETE ----------
async def delete_user(user_id: str) -> UserOut:
    user = await User.get(user_id)
    if not user:
        raise UserNotFound()

    await user.delete()
    logger.info(f"Usuário deletado: {user_id}")
    return UserOut(**user.dict())
