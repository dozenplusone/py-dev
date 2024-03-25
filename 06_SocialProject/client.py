import cmd
import socket


class ChatCmd(cmd.Cmd):
    def __init__(self, sockfd: socket.socket):
        super().__init__()
        self.sockfd = sockfd

    def do_login(self, arg):
        self.sockfd.sendall(f"login {arg.split()[0]}\n".encode())
        print(self.sockfd.recv(1024).decode().rstrip())

    def do_who(self, arg):
        if arg:
            print("error: 'who' takes no arguments")
        else:
            self.sockfd.sendall(b"who\n")
            print(self.sockfd.recv(1024).decode().rstrip())

    def do_cows(self, arg):
        if arg:
            print("error: 'cows' takes no arguments")
        else:
            self.sockfd.sendall(b"cows\n")
            print(self.sockfd.recv(1024).decode().rstrip())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockfd:
    sockfd.connect(("localhost", 1337))
    ChatCmd(sockfd).cmdloop()
