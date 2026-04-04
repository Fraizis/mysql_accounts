import psycopg2

# Connect to the School database
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password="postgres",
    host="localhost"
)

cur = conn.cursor()

sql = """
INSERT INTO users(id, name) VALUES (%s, %s);
"""

val = ((1, "Ram"), (2, "CSE"), (3, "85"), (4, "B"), (5, "19"))

# cur.executemany(sql, val)

conn.commit()

sql_new = """
SELECT * FROM USERS;
"""

cur.execute(sql_new)

myresult = cur.fetchall()
print(myresult)


cur.close()
conn.close()
