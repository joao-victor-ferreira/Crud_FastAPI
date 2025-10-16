from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.v1.routes import user_routes, auth_routes  # ⬅ importa o novo arquivo
from dotenv import load_dotenv
import os
import logging

# Carrega variáveis do .env
load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

# Configurações da API
PROJECT_NAME = os.getenv("PROJECT_NAME", "User CRUD API")
API_VERSION = os.getenv("API_VERSION", "1.0.0")
API_DESCRIPTION = os.getenv(
    "API_DESCRIPTION",
    "API completa de CRUD de usuários com FastAPI e MongoDB (Beanie), incluindo autenticação JWT."
)

app = FastAPI(
    title=PROJECT_NAME,
    version=API_VERSION,
    description=API_DESCRIPTION,
)

# Inicialização do banco de dados
@app.on_event("startup")
async def startup_event():
    logger.info("Inicializando banco de dados...")
    await init_db()
    logger.info("Banco de dados inicializado com sucesso!")

# Incluindo rotas
app.include_router(user_routes.router, prefix="/api/v1", tags=["Users"])
app.include_router(auth_routes.router, prefix="/api/v1", tags=["Auth"])
