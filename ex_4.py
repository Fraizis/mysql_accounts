from sqlalchemy import text

from settings import engine

# 4. Сформируйте выборку, которая содержит счета, относящиеся к продуктам
# типа ДЕПОЗИТ или КАРТА, по которым были операции внесения средств на
# счет в рамках одного произвольного дня.


q_4 = """
SELECT DISTINCT a.*
FROM accounts AS a
JOIN products AS p ON p.id = a.product_ref
JOIN product_type AS pt ON 
    p.product_type_id = pt.id AND 
    pt.name IN ('депозит', 'карта')
JOIN records AS r ON 
    r.acc_ref = a.id AND 
    r.dt = 1 AND 
    DATE(r.oper_date) = '2026-04-04';
"""

if __name__ == '__main__':
    with engine.connect() as con:
        db = con.execute(text(q_4))
        for i in db.fetchall():
            print(i)
