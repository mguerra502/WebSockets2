# Websocket server example

import asyncio
import websockets
import json
import pprint

async def hello(websocket, path):
	name = await websocket.recv()
	print(f"<{name}")

	greeting = {
		'name': name,
		'age': 30,
		'city': 'Dublin'
	}
	
	await websocket.send(json.dumps(greeting))
	pprint(f"> {greeting}")

try:
	start_server = websockets.serve(hello, 'localhost', 8765)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()
except TypeError:
	print("Good Bye!")