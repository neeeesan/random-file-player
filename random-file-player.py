import os
import random
from pathlib import Path

""" Add any extensions that you want to ignore, for example subtitle or readme files """
ext = (".srt", ".ass", ".sub", ".txt", ".nfo", ".db")


""" Replace with the path of the folder you want to play from """
f = Path(r"D:\Videos\The Big Bang Theory")


def open_file(file_name):
    try:
        os.startfile(file_name)
    except Exception as e:
        print("Error", str(e))


def rand_file(f):
    f = [x for x in f.rglob("*") if x.is_file() and x.suffix not in ext]
    file = random.choice(f)
    print(file.name)
    open_file(file)


if __name__ == '__main__':
    rand_file(f)
