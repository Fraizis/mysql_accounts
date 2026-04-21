from loguru import logger
from mysql import connector

from main import mysql_connect

# В результате сбоя в базе данных разъехалась информация между остатками
# и операциями по счетам. Напишите нормализацию (процедуру выравнивающую данные),
# которая найдет такие счета и восстановит остатки по счету. Необходимо таким
# клиентам выплатить компенсацию в размере 1% от восстановленного остатка счета
# (для счетов, относящихся к продукту типа ДЕПОЗИТ).


q_6 = """
WITH ac AS (
	SELECT
		r.acc_ref,
		(SUM(CASE WHEN r.dt = 1 THEN `sum` ELSE 0 END) -
		SUM(CASE WHEN r.dt = 0 THEN `sum` ELSE 0 END)) AS new_saldo
	FROM accounts AS a
	JOIN products AS p ON p.id = a.product_ref
	JOIN product_type AS pt ON p.product_type_id = pt.id AND pt.name = 'депозит'
	JOIN records AS r ON r.acc_ref = a.id
	GROUP BY acc_ref
)
UPDATE accounts AS a 
SET saldo = (SELECT new_saldo + ABS(new_saldo * 0.01) FROM ac WHERE acc_ref = a.id)
WHERE EXISTS (SELECT new_saldo + ABS(new_saldo * 0.01) FROM ac WHERE acc_ref = a.id); 
"""


def query_6(conn):
    try:
        cur = conn.cursor()
        cur.execute(q_6)
        cur.fetchmany()
        logger.info(f"Results for: {q_6}")

        logger.info('Saldo changed')

        cur.close()
        conn.close()

    except connector.Error as err:
        logger.error(f"Произошла ошибка: {err}")


if __name__ == '__main__':
    conn = mysql_connect()
    query_6(conn)
