import asyncio
import asyncpg


async def add_item(category_id, url, name, price):
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    print(name, category_id)
    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')
    # Execute a statement to create a new table.

    # Insert a record into the created table.
    await conn.execute('''
        INSERT INTO items(category_id, name, price, url) VALUES($1, $2, $3, $4)
    ''', category_id, name, price, url)

    # Close the connection.
    await conn.close()

# asyncio.get_event_loop().run_until_complete(add_category(1, 'test', 'var'))




