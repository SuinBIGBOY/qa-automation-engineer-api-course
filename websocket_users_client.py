import asyncio
import websockets

async def client():
    async with websockets.connect('ws://localhost:8765') as ws:
        message = "Привет, сервер!"
        print(f'Отправка {message}')
        await ws.send(message)
        for _ in range(5):
            message = await ws.recv()
            print(message)


asyncio.run(client())