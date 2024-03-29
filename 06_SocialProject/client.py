import cmd
import readline
import shlex
import socket
import threading


class ChatCmd(cmd.Cmd):
    prompt = ''

    def __init__(self, sockfd: socket.socket):
        super().__init__()
        self.sockfd = sockfd
        self.listening = threading.Event()
        self.listening.set()

    def do_login(self, arg):
        self.sockfd.sendall(f"login {arg.split()[0]}\n".encode())

    def do_who(self, arg):
        if arg:
            print("error: 'who' takes no arguments")
        else:
            self.sockfd.sendall(b"who\n")

    def do_cows(self, arg):
        if arg:
            print("error: 'cows' takes no arguments")
        else:
            self.sockfd.sendall(b"cows\n")

    def do_say(self, arg):
        args = shlex.split(arg)
        self.sockfd.sendall(f"say {shlex.join(args[:2])}\n".encode())

    def do_yield(self, arg):
        args = shlex.split(arg)
        self.sockfd.sendall(f"yield {shlex.join(args[:1])}\n".encode())

    def do_quit(self, arg):
        if arg:
            print("error: 'quit' takes no arguments")
        else:
            self.sockfd.sendall(b"quit\n")
            self.sockfd = None
            return True

    do_EOF = do_quit

    def complete_login(self, text, line, begidx, endidx):
        self.listening.clear()
        self.sockfd.sendall(b"cows\n")
        cows = self.sockfd.recv(384).decode().split()
        self.listening.set()
        return [c for c in cows if c.startswith(text)]

    def complete_say(self, text, line, begidx, endidx):
        last = shlex.split(line)[-2 if text else -1]
        if last == "say":
            self.listening.clear()
            self.sockfd.sendall(b"who\n")
            cows = self.sockfd.recv(384).decode().split()
            self.listening.set()
            return [c for c in cows if c.startswith(text)]


def listen(cmdline: ChatCmd):
    while cmdline.sockfd is not None:
        cmdline.listening.wait()
        data = b''
        while len(new := cmdline.sockfd.recv(1024)) == 1024:
            data += new
        data += new
        print(f"\n{data.decode().rstrip()}",
              f"\n{cmdline.prompt}{readline.get_line_buffer()}",
              sep='', end='', flush=True)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockfd:
    sockfd.connect(("localhost", 1337))
    cmdline = ChatCmd(sockfd)
    threading.Thread(target=listen, args=(cmdline,)).start()
    threading.Thread(target=cmdline.cmdloop()).start()
