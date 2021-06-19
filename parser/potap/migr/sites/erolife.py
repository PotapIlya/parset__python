import asyncio
import asyncpg


async def create_sites():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://postgres@127.0.0.1/postgres')
    # Execute a statement to create a new table.

    # Insert a record into the created table.
    await conn.execute('''
        INSERT INTO sites(name, url) VALUES($1, $2, $3)
    ''', 'Эролайф', 'https://erolaif.ru/', 'shop')

    # Select a row from the table.
    # row = await conn.fetchrow(
    #     'SELECT * FROM users WHERE name = $1', 'Bob')
    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()

asyncio.get_event_loop().run_until_complete(create_sites())