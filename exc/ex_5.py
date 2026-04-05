from sqlalchemy import text

from settings import engine

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

if __name__ == '__main__':
    with engine.connect() as con:
        con.execute(text('USE shift_cftbank'))

        res = con.execute(text(q_5))

        for i in res.fetchall():
            print(i)
