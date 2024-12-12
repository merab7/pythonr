import asyncio


# Define a coroutine that simulates a tim-consuming task
async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to ftech data.")
    await asyncio.sleep(sleep_time)  # simulate an I/O operation with sleep
    return {"id": id, "data": f"Sample data form coroutine{id}"}


async def main():
    # Create task for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)


# after main() dunction is colled it returns coroutine object with
# should be awaited for it to be accecuted

# Run the main coroutine
asyncio.run(main())
