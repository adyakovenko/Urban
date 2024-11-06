import asyncio
from turtledemo.penrose import start


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {ball_number} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha',   3))
    task2 = asyncio.create_task(start_strongman('Denis',   4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1, task2, task3

if __name__ == '__main__':
    asyncio.run(start_tournament())
