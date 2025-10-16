import logging
from logging.handlers import RotatingFileHandler
import os

# Cria diretório de logs se não existir
LOG_DIR = os.getenv("LOG_DIR", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração do logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)  # Nível mínimo de log

# Formato dos logs
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Handler para console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Handler para arquivo (rotativo)
file_handler = RotatingFileHandler(
    filename=os.path.join(LOG_DIR, "app.log"),
    maxBytes=5 * 1024 * 1024,  # 5 MB por arquivo
    backupCount=5
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
