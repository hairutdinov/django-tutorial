from pathlib import Path

from envparse import Env

env = Env()

ROOT_DIR = Path(__file__).resolve().parent.parent

env.read_envfile(ROOT_DIR / ".env")

DB_HOST = env.str("DB_HOST", default="localhost")
DB_NAME = env.str("DB_NAME", default="postgres")
DB_USERNAME = env.str("DB_USERNAME", default="postgres")
DB_PASSWORD = env.str("DB_PASSWORD", default="postgres")
DB_EXPOSE_PORT = env.int("DB_EXPOSE_PORT", default=5432)
DB_PORT = env.int("DB_PORT", default=5432)
