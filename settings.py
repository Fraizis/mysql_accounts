from sqlalchemy import create_engine

user = "root"
password = "09021991qqQ"
host = "127.0.0.1"
port = 3306
database = "shift_cftbank"


mysql_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}"

engine = create_engine(mysql_uri)
