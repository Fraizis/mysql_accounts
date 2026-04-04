from sqlalchemy import text

from settings import engine


q_5 = """
WITH ac AS (
	SELECT DISTINCT a.id
	FROM accounts AS a
	JOIN products AS p ON p.id = a.product_ref
	JOIN product_type AS pt ON p.product_type_id = pt.id AND pt.name = 'кредит'
),
ct1 AS (
	SELECT ac.id, SUM(`sum`) AS summ
	FROM records r
	JOIN ac ON ac.id = r.acc_ref
	WHERE dt = 1
	GROUP BY acc_ref
),
ct2 AS (
	SELECT ac.id, SUM(`sum`) AS summ
	FROM records r
	JOIN ac ON ac.id = r.acc_ref
	WHERE dt = 0
	GROUP BY acc_ref
),
ct3 AS (
	SELECT ct1.id
	FROM ct1 
	JOIN ct2 ON ct2.id = ct1.id
	WHERE ct1.summ > ct2.summ
)
SELECT c.*
FROM clients c
JOIN accounts a ON a.client_ref = c.id
JOIN ct3 ON ct3.id = a.id;
"""

if __name__ == '__main__':
    with engine.connect() as con:
        db = con.execute(text(q_5))
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
