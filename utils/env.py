from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
dialect = os.getenv("DB_DIALECT")
driver = os.getenv("DB_DRIVER")

SQLALCHEMY_DATABASE_URI = f"{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}"
