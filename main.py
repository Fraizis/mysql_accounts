from sqlalchemy import create_engine, text
import mysql.connector as connector

user = "root"
password = "09021991qqQ"
host = "127.0.0.1"
port = 3306
database = "shift_cftbank"


# Строка подключения к MySQL
mysql_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Создание движка
engine = create_engine(mysql_uri)

# -- 4. Сформируйте выборку, которая содержит счета, относящиеся к продуктам
# --     типа ДЕПОЗИТ или КАРТА, по которым были операции внесения средств на
# --     счет в рамках одного произвольного дня.


q_4 = """
SELECT DISTINCT a.*
FROM accounts AS a
JOIN products AS p ON p.id = a.product_ref
JOIN product_type AS pt ON p.product_type_id = pt.id AND pt.name IN ('депозит', 'карта')
JOIN records AS r ON r.acc_ref = a.id AND r.dt = 1 AND DATE(r.oper_date) = '2026-04-04';
"""

if __name__ == '__main__':
    with engine.connect() as con:
        db = con.execute(text(q_4))
        for i in db.fetchall():
            print(i)

    # import mysql.connector
    # from mysql.connector import Error
    #
    # try:
    #     connection = mysql.connector.connect(
    #         host='localhost',
    #         database='shift_cftbank',
    #         user='root',
    #         password='09021991qqQ'
    #     )
    #     if connection.is_connected():
    #         db_Info = connection.get_server_info()
    #         print("Connected to MySQL Server version ", db_Info)
    #         cur = connection.cursor()
    #
    #         cur.execute("select database();")
    #         record = cur.fetchone()
    #         print("You're connected to database: ", record)
    #
    #         cur.execute('SELECT * FROM accounts')
    #         # record = cur.fe
    #         for i in cur.fetchall():
    #             print(i)
    #
    #         cur.close()
    #         connection.close()
    #
    # except Error as e:
    #     print("Error while connecting to MySQL", e)
