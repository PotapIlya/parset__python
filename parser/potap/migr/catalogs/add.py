import asyncio
import asyncpg


async def add_category(site_id, url, name, pars):
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    print(name, pars)
    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')
    # Execute a statement to create a new table.

    # Insert a record into the created table.
    await conn.execute('''
        INSERT INTO categories(site_id, url, name, pars_cat_id) VALUES($1, $2, $3, $4)
    ''', site_id, url, name, pars)

    # Close the connection.
    await conn.close()

# asyncio.get_event_loop().run_until_complete(add_category(1, 'test', 'var'))




