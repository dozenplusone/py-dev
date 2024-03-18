import asyncio
import cowsay
import shlex


clients = {}


async def cowChat(reader, writer):
    async def cmdExec(cmd: str):
        nonlocal buffer, login
        match shlex.split(cmd):
            case ["login", _login]:
                if (_login in cowsay.list_cows()
                        and _login not in clients
                        and buffer not in clients.values()):
                    login = _login
                    clients[login] = buffer
                    await buffer.put("Login successful")
                else:
                    await buffer.put("Login failed")

    login = None
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
