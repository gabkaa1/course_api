import asyncio
import time 
import aiosqlite

async def setup_db() :
    global db
    db = await aiosqlite.connect('db_example.db')
    await db.execute("DROP TABLE IF EXISTS user")
    await db.execute("CREATE TABLE user (id int)") 
    await db.execute("INSERT INTO user VALUES (1)") 
    await db.execute("""
                     INSERT INTO user
                     WITH RECURSIVE cte(x) AS (
                     SELECT random()
                     UNION ALL
                     SELECT random()
                     FROM cte
                     LIMIT 4000000
                     )
                     SELECT x FROM cte;
                     """)
    # WITH RECURSIVE cte — создаёт рекурсивный обобщённый табличный выражение (CTE)
    # UNION ALL — объединяет начальное значение со всеми рекурсивными

    await db.commit()
    print ("DB Created")

async def get_large_data():
    print('start - large')
    cursor = await db.execute('SELECT * FROM user')
    rows = await cursor.fetchall()
    print('end - large', len(rows))
    return rows

async def get_small_data():
    print('start - small')
    cursor = await db.execute('SELECT * FROM user WHERE id=1')
    rows = await cursor.fetchall()
    print('end - small', len(rows))
    return rows

async def main1():
    await setup_db()

    start = time.perf_counter()

    await get_large_data()
    await get_small_data()

    end = time.perf_counter()
    print(f'lasts for: {end-start:.2f}')

async def main2():
    await setup_db()

    start = time.perf_counter()

    task1 = asyncio.create_task(get_large_data())
    task2 = asyncio.create_task(get_small_data())
    await task1
    await task2

    end = time.perf_counter()
    print(f'lasts for: {end-start:.2f}')

if __name__ == '__main__':
    try:
        asyncio.run(main2())
    except (Exception, KeyboardInterrupt) as e:
        print('error', str(e))
        exit()