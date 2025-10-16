# FastAPI Backend Project

## Descrição

Projeto backend em **FastAPI** para gerenciamento de usuários, implementando **CRUD completo**, **hashing de senha**, **JWT**, **logging** e **testes assíncronos** com `pytest-asyncio`.

O banco de dados utilizado é **MongoDB Atlas**, usando **Beanie ODM**.

Este projeto é construído com arquitetura modular de nível sênior, separando responsabilidades em **rotas**, **serviços**, **schemas**, **modelos** e **configuração**.

---

## Estrutura do Projeto

```
FASTAPI-BACKEND/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           ├── auth_routes.py       # Rotas de autenticação
│   │           └── user_routes.py       # Rotas CRUD de usuários
│   ├── core/
│   │   ├── config.py                     # Configurações do projeto e .env
│   │   ├── logger.py                     # Configuração de logging
│   │   └── security.py                   # Hash de senha e JWT
│   ├── db/
│   │   ├── models/
│   │   │   └── user_model.py             # Modelos Beanie
│   │   └── init_db.py                    # Inicialização do MongoDB
│   ├── exceptions/
│   │   └── user_exceptions.py            # Exceções customizadas
│   ├── schemas/
│   │   └── user_schemas.py               # Schemas Pydantic
│   ├── services/
│   │   ├── auth_services.py              # Serviços de autenticação
│   │   └── user_services.py              # Serviços CRUD
│   └── main.py                            # Inicialização do FastAPI
├── logs/
│   └── app.log                            # Arquivo de logs
├── tests/
│   ├── conftest.py                        # Fixture async_client para testes
│   └── test_users.py                       # Testes CRUD de usuários
├── venv/                                  # Ambiente virtual Python
└── .env                                   # Variáveis de ambiente
```

---

## Tecnologias e Bibliotecas Utilizadas

* **Python 3.13**
* **FastAPI**: Framework web moderno e assíncrono
* **Uvicorn**: Servidor ASGI
* **Beanie**: ODM para MongoDB baseado em Pydantic
* **Motor**: Driver assíncrono para MongoDB
* **Pydantic**: Validação de dados e schemas
* **Python-Jose**: JWT (JSON Web Tokens)
* **pytest + pytest-asyncio**: Testes assíncronos
* **httpx**: Cliente HTTP assíncrono para testes
* **asgi_lifespan**: Gerenciamento de eventos de startup/shutdown no FastAPI
* **Logging**: Registro de eventos e erros do sistema

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
MONGODB_URI=mongodb+srv://usuario:senha@cluster.mongodb.net/banco
DB_NAME=projetos
PROJECT_NAME=FastAPI Server Base
API_VERSION=v1
SECRET_KEY=SUA_CHAVE_SECRETA
ALGORITHM=HS256
```

---

## Instalação

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

> Caso não tenha o `requirements.txt`, instale manualmente:

```bash
pip install fastapi uvicorn beanie motor pydantic python-jose pytest pytest-asyncio httpx asgi_lifespan bcrypt python-dotenv
```

---

## Executando o Projeto

Para rodar o servidor FastAPI:

```bash
uvicorn app.main:app --reload
```


---

## Estrutura de Rotas

### CRUD de Usuários (`/api/v1/users`)

* `GET /users` → Lista todos os usuários
* `GET /users/{user_id}` → Obter usuário por ID
* `POST /users` → Criar usuário
* `PUT /users/{user_id}` → Atualizar usuário
* `DELETE /users/{user_id}` → Deletar usuário

### Autenticação (`/api/v1/auth`)

* `POST /auth/login` → Retorna JWT

---

## Testes

Todos os testes usam `pytest-asyncio` + `httpx.AsyncClient`:

```bash
# Com PYTHONPATH
PYTHONPATH=. pytest -v
```

* Testes cobrem todas as operações CRUD de usuário.
* Utiliza fixture `async_client` com `asgi_lifespan` para simular o app sem precisar rodar o servidor.

---

## Logging

* Logs ficam em `logs/app.log`
* Nível de logs configurável em `app/core/logger.py`

Exemplos de uso:

```python
logger.info("Usuário criado com sucesso")
logger.warning("Tentativa de criar usuário com e-mail existente")
logger.error("Usuário não encontrado")
```

---

## Observações

* O projeto é **assíncrono** e pronto para produção.
* Estrutura modular facilita **manutenção** e **escalabilidade**.
* JWT e hashing de senha já implementados para autenticação.
* Testes assíncronos garantem qualidade de código e estabilidade do CRUD.

---

## Contato

Para dúvidas ou melhorias, abra uma issue no repositório.
