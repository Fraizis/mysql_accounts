import sqlite3

from main import mysql_uri

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

if __name__ == '__main__':
    with sqlite3.connect(f'../{mysql_uri}') as conn:
        cursor = conn.cursor()

        res = cursor.execute(q_3)

        for i in res.fetchall():
            print(i)
