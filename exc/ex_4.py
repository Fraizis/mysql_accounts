from loguru import logger
from mysql import connector

from main import mysql_connect

# Сформируйте выборку, которая содержит счета, относящиеся к продуктам
# типа ДЕПОЗИТ или КАРТА, по которым были операции внесения средств на
# счет в рамках одного произвольного дня.


q_4 = """
SELECT 
    DISTINCT a.*
FROM 
    accounts AS a
JOIN products AS p ON 
    p.id = a.product_ref
JOIN product_type AS pt ON 
    p.product_type_id = pt.id AND 
    pt.name IN ('депозит', 'карта')
JOIN records AS r ON 
    r.acc_ref = a.id AND 
    r.dt = 1 AND 
    DATE(r.oper_date) = %s;
"""


def query_4(conn, operation_date):
    try:
        cur = conn.cursor()
        cur.execute(q_4, (operation_date,))
        result = cur.fetchall()
        logger.info(f"Results for: {q_4}")

        for r in result:
            logger.info(r)

        cur.close()
        conn.close()

    except connector.Error as err:
        logger.error(f"Произошла ошибка: {err}")


if __name__ == '__main__':
    oper_date = '2026-04-21'
    conn = mysql_connect()
    query_4(conn, operation_date=oper_date)
