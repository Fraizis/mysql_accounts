import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')

mysql_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}"
engine = create_engine(mysql_uri)
