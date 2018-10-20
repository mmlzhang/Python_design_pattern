
"""

    命令模式
"""

import os

verbose = True


class RenameFile(object):

    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}]".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.dest, self.src)


class CreateFile(object):
    def __init__(self, path, txt):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print("[create file '{}']".format(self.path))
        with open(self.path, mode="w", encoding="utf-8") as out_file:
            out_file.write(self.txt)

    def undo(self):
        os.remove(self.path)


class ReadFile(object):
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, 'r', encoding="utf-8") as in_file:
            print(in_file.read(), end="")


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in [CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name)]:
        commands.append(cmd)

    [c.execute() for c in commands]

    anwser = input("reverse the executed commands? [y/n]")

    if anwser not in "Yy":
        print("the result is {}".format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == '__main__':
    main()
