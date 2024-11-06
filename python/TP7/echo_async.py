import asyncio, socket

async def handle_client(reader, writer):
    pass

async def run_server():
    port=49631
    server = await asyncio.start_server(handle_client, 'localhost', port)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())