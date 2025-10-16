import os
import certifi
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.db.models.user_model import User
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError

load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("init_db")

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME", "projetos")
SERVER_SELECTION_TIMEOUT_MS = int(os.getenv("MONGO_TIMEOUT_MS", 10000))

async def init_db():
    if not MONGODB_URI:
        raise Exception("MONGODB_URI não definido no .env")

    try:
        client = AsyncIOMotorClient(
            MONGODB_URI,
            tls=True,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=SERVER_SELECTION_TIMEOUT_MS
        )
        db = client[DB_NAME]

        # Teste de conexão
        await db.command("ping")
        logger.info(f"MongoDB conectado com sucesso! Database: {DB_NAME}")

        # Inicializa Beanie com os modelos
        await init_beanie(database=db, document_models=[User])
        logger.info("Beanie inicializado com sucesso!")

    except ServerSelectionTimeoutError as e:
        logger.error(f"Erro de conexão com MongoDB: {e}")
        raise ConnectionError("Não foi possível conectar ao MongoDB. Verifique a URI e a rede.") from e
    except Exception as e:
        logger.error(f"Erro ao inicializar banco de dados: {e}")
        raise
