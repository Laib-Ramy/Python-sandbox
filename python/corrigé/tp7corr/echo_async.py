import asyncio, socket

async def handle_client(reader, writer):
    request = None
    while request != 'quit':
        request = (await reader.read(255)).decode('utf8')
        response = "echo: "+str(request)
        writer.write(response.encode('utf8'))
        await writer.drain()
    writer.close()

async def run_server():
    port=49631
    server = await asyncio.start_server(handle_client, 'localhost', port)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())