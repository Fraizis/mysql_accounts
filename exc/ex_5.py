from loguru import logger
from mysql import connector

from main import mysql_connect

# Найдите клиентов, у которых открыт продукт типа КРЕДИТ, и у которых
# сумма всех дебетовых операций по таким продуктам превышает сумму всех
# кредитовых операций.


q_5 = """
WITH ac AS (
	SELECT 
		r.acc_ref,
		a.client_ref,
		SUM(CASE WHEN r.dt = 1 THEN `sum` ELSE 0 END) AS sum_db,
		SUM(CASE WHEN r.dt = 0 THEN `sum` ELSE 0 END) AS sum_cr
	FROM accounts AS a
	JOIN products AS p ON p.id = a.product_ref
	JOIN product_type AS pt ON p.product_type_id = pt.id AND pt.name = 'кредит'
	JOIN records AS r ON r.acc_ref = a.id
	GROUP BY acc_ref 
)
SELECT *
FROM clients c
JOIN ac ON client_ref = c.id
WHERE sum_db > sum_cr;
"""


def query_5(conn):
    try:
        cur = conn.cursor()
        cur.execute(q_5)
        result = cur.fetchall()
        logger.info(f"Results for: {q_5}")

        for r in result:
            logger.info(r)

        cur.close()
        conn.close()

    except connector.Error as err:
        logger.error(f"Произошла ошибка: {err}")


if __name__ == '__main__':
    conn = mysql_connect()
    query_5(conn)
