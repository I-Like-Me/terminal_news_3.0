from sqlalchemy import create_engine
from config import Config
import psycopg2

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
