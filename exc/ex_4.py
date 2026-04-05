from sqlalchemy import text

from settings import engine

# 4. Сформируйте выборку, которая содержит счета, относящиеся к продуктам
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
    DATE(r.oper_date) = :date_search;
"""

if __name__ == '__main__':
    with engine.connect() as con:
        con.execute(text('USE shift_cftbank'))

        res = con.execute(text(q_4), {'date_search': '2026-04-05'})

        for i in res.fetchall():
            print(i)
