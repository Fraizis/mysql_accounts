import sqlite3

from main import mysql_uri

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
    DATE(r.oper_date) = :date_search;
"""

if __name__ == '__main__':
    with sqlite3.connect(f'../{mysql_uri}') as conn:
        cursor = conn.cursor()

        res = cursor.execute(q_4, {'date_search': '2026-04-06'})

        for i in res.fetchall():
            print(i)
