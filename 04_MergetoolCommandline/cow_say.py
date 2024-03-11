import cmd
import cowsay
import shlex


def parseArgs(s):
    args = shlex.split(s)
    assert len(args) & 1 == 0
    return dict(zip(args[::2], args[1::2]))


class CowShell(cmd.Cmd):
    __eyes = "==", "XX", "$$", "@@", "**", "--", "OO", "..", "bd"
    __tongue = "\"U \"", "\"\\/\"", "\" V\""
    __params = "message", "eyes", "tongue", "cow"

    def do_list_cows(self, arg):
        """list_cows
        List available cows."""
        print("Built-in cow files:")
        print(*sorted(cowsay.list_cows()))

    def do_make_bubble(self, arg):
        """make_bubble text TEXT
        Make a cowsay's bubble containing TEXT."""
        print(cowsay.make_bubble(**parseArgs(arg)))

    def do_cowsay(self, arg):
        """cowsay message MESSAGE [eyes EYES] [tongue TONGUE] [cow COW]
        Draw a COW with EYES and TONGUE saying MESSAGE."""
        print(cowsay.cowsay(**parseArgs(arg)))

    def do_cowthink(self, arg):
        """cowthink message MESSAGE [eyes EYES] [tongue TONGUE] [cow COW]
        Same as cowsay (see: help cowsay), but with different bubble style."""
        print(cowsay.cowthink(**parseArgs(arg)))

    def complete_cowsay(self, text, line, begidx, endidx):
        last = shlex.split(line)[-2 if text else -1]
        if last == "eyes":
            return [e for e in self.__class__.__eyes if e.startswith(text)]
        elif last == "tongue":
            return [t for t in self.__class__.__tongue if t.startswith(text)]
        elif last == "cow":
            return [c for c in cowsay.list_cows() if c.startswith(text)]
        else:
            return [p for p in self.__class__.__params if p.startswith(text)]

    complete_cowthink = complete_cowsay


if __name__ == '__main__':
    CowShell().cmdloop()
