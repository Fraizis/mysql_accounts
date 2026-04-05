from sqlalchemy import text

from settings import engine

# -- 6. В результате сбоя в базе данных разъехалась информация между остатками
# --     и операциями по счетам. Напишите нормализацию (процедуру выравнивающую данные),
# --     которая найдет такие счета и восстановит остатки по счету. Необходимо таким
# --     клиентам выплатить компенсацию в размере 1% от восстановленного остатка счета
# --     (для счетов, относящихся к продукту типа ДЕПОЗИТ).


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
UPDATE accounts a
JOIN ac ON ac.acc_ref = a.id
SET saldo = (new_saldo + ABS(new_saldo * 0.01)); 
"""


if __name__ == '__main__':
    with engine.connect() as con:
        con.execute(text('USE shift_cftbank'))

        con.execute(text(q_6))
        con.commit()
        print('Saldo changed')
