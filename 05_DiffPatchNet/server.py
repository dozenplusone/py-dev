import asyncio
import cowsay


clients = {}


async def cowChat(reader, writer):
    pass


async def main():
    server = await asyncio.start_server(cowChat, "localhost", 1337)
    async with server:
        await server.serve_forever()


asyncio.run(main())
