import asyncio
import asyncpg


async def create_catalogs():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')
    # Execute a statement to create a new table.
    await conn.execute('''
        CREATE TABLE categories(
            id serial PRIMARY KEY,
            site_id int,
            url text,
            name text,
            pars_cat_id int
        )
    ''')

    # Close the connection.
    await conn.close()

asyncio.get_event_loop().run_until_complete(create_catalogs())


# rollback

