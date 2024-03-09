import cmd
import cowsay
import shlex


class CowShell(cmd.Cmd):
    pass


if __name__ == '__main__':
    CowShell().cmdloop()
