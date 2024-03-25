import cmd
import readline
import socket
import threading


class ChatCmd(cmd.Cmd):
    prompt = ''

    def __init__(self, sockfd: socket.socket):
        super().__init__()
        self.sockfd = sockfd

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


def listen(cmdline: ChatCmd):
    while True:
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
    cmdline.cmdloop()
