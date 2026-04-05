from sqlalchemy import text

from settings import engine


# if __name__ == '__main__':
#     with engine.connect() as con:
#         db = con.execute(text(q_5))
#         for i in db.fetchall():
#             print(i)
