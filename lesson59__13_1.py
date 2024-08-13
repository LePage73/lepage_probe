# Домашнее задание по теме "Асинхронность на практике"

import asyncio


async def start_strongman(name, power):
        print(f'Силач "{name}" начал соревнования.')
        for boll_ in range(1,6):
            await asyncio.sleep(1 / power)
            print(f'Силач "{name}" поднял {boll_} шар')
        print(f'Силач "{name}" закончил соревнования.')

async def start_tournament():
        task_1 = asyncio.create_task(start_strongman('Arnold S.', 3))
        task_2 = asyncio.create_task(start_strongman('Sylvester S.', 2))
        task_3 = asyncio.create_task(start_strongman('Jean-Claude V.D.', 1))
        await  task_1
        await  task_2
        await  task_3


asyncio.run(start_tournament())