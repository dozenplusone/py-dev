import asyncio
import cowsay


clients = {}


async def cowChat(reader, writer):
    async def cmdExec(cmd: str):
        nonlocal buffer
        await buffer.put(cmd)

    buffer = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(buffer.get())
    while not reader.at_eof():
        done, pending = await asyncio.wait(
            [send, receive],
            return_when=asyncio.FIRST_COMPLETED
        )
        for task in done:
            if task is send:
                send = asyncio.create_task(reader.readline())
                await cmdExec(task.result().decode())
            elif task is receive:
                receive = asyncio.create_task(buffer.get())
                writer.write(f"{task.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(cowChat, "localhost", 1337)
    async with server:
        await server.serve_forever()


asyncio.run(main())
