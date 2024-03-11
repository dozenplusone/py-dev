import cmd
import cowsay
import shlex


def parseArgs(s):
    args = shlex.split(s)
    assert len(args) & 1 == 0
    return dict(zip(args[::2], args[1::2]))


class CowShell(cmd.Cmd):
    def do_list_cows(self, arg):
        print("Built-in cow files:")
        print(*sorted(cowsay.list_cows()))

    def do_make_bubble(self, arg):
        print(cowsay.make_bubble(**parseArgs(arg)))

if __name__ == '__main__':
    CowShell().cmdloop()
