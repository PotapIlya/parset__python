import psycopg2
import asyncpg


async def create_sql(title, price, href, text, type_id):

    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')

    await conn.execute('''
        INSERT INTO potap (title, price, href, text, type_id) VALUES($1, $2, $3, $4, $5)
    ''', title, price, href, text, type_id)

    await conn.close()


async def check_sql(type_id):

    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')
    row = await conn.fetchrow(
        'SELECT * FROM potap WHERE type_id = $1', type_id)
    await conn.close()

    if row:
        return False
    else:
        return True


    # conn = psycopg2.connect(database="postgres", user="postgres", password="", host="127.0.0.1", port="5432")
    # cur = conn.cursor()
    #
    # cur.execute('SELECT * FROM potap WHERE type_id = %s', (type_id,))
    # row = cur.fetchall()
    # conn.commit()
    # conn.close()
    #
    # if len(row) == 1:
    #     return False
    # else:
    #     return True
