from loguru import logger
from mysql import connector

from main import mysql_connect

# Сформируйте отчет, который содержит все счета, относящиеся к продуктам
# типа ДЕПОЗИТ, принадлежащих клиентам, у которых имеется более одного открытого продукта.


q_3 = """
WITH cl AS (
	SELECT 
	    p.id, 
	    p.client_ref, 
	    COUNT(p.id) OVER(PARTITION BY p.client_ref) AS pc
	FROM products AS p
	JOIN product_type AS pt ON p.product_type_id = pt.id
	WHERE pt.name = 'депозит'
)
SELECT * 
FROM accounts AS a
JOIN cl ON 
	cl.client_ref = a.client_ref AND 
	a.product_ref = cl.id AND 
	pc > 1;
"""


def query_3(conn):
    try:
        cur = conn.cursor()
        cur.execute(q_3)
        result = cur.fetchall()
        logger.info(f"Results for: {q_3}")

        for r in result:
            logger.info(r)

        cur.close()
        conn.close()

    except connector.Error as err:
        logger.error(f"Произошла ошибка: {err}")


if __name__ == '__main__':
    conn = mysql_connect()
    query_3(conn)
