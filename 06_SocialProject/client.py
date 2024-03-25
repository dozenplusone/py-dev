import cmd
import socket


class ChatCmd(cmd.Cmd):
    def __init__(self, sockfd: socket.socket):
        super().__init__()
        self.sockfd = sockfd


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockfd:
    sockfd.connect(("localhost", 1337))
    ChatCmd(sockfd).cmdloop()
