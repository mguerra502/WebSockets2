# Websocket client example

import asyncio
import websockets
from pprint import pprint
import json

async def hello():
	async with websockets.connect('ws://localhost:8765') as websocket:
		name = input("What's your name? ")

		await websocket.send(name)
		print(f"> {name}")

		greeting = await websocket.recv()
		pprint(json.loads(greeting))


asyncio.get_event_loop().run_until_complete(hello())