import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
load_dotenv()
url = os.getenv("CONNECTION_STRING")
result = urlparse(url)
query_params = parse_qs(result.query)
sslmode = query_params.get("sslmode", ["require"])[0]

ASYNC_DB_URL = f"postgresql+asyncpg://{result.username}:{result.password}@{result.hostname}:{result.port or 5432}/{result.path[1:]}?sslmode={sslmode}"

Base = declarative_base()

engine= create_async_engine(ASYNC_DB_URL, echo=True)
