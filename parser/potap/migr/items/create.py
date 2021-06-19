import asyncio
import asyncpg


async def create_items():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')
    # Execute a statement to create a new table.
    await conn.execute('''
        CREATE TABLE items(
            id serial PRIMARY KEY,
            category_id int,
            name text,
            price text,
            url text
        )
    ''')

    # Close the connection.
    await conn.close()

asyncio.get_event_loop().run_until_complete(create_items())


# rollback

