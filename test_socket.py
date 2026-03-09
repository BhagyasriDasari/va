import asyncio
import websockets

async def test():

    uri = "ws://127.0.0.1:8000/voice"

    async with websockets.connect(uri) as websocket:

        await websocket.send("book appointment")

        response = await websocket.recv()

        print(response)

asyncio.run(test())