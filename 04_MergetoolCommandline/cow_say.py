import cmd
import cowsay
import shlex


class CowShell(cmd.Cmd):
    def do_list_cows(self, arg):
        print("Built-in cow files:")
        print(*sorted(cowsay.list_cows()))


if __name__ == '__main__':
    CowShell().cmdloop()
