# This is a sample Python script.
from pathlib import Path
import argparse
from findfivers.custom_argparse import ArgsNamespace
import pandas as pd


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def write_result(result):
    df = pd.DataFrame(list(result), columns=['the_word'], index=None)
    df.to_csv('result3.csv', sep=',', index=False)


def find_five(cliargs):
    file = Path(cliargs.filename)
    # destination = Path("result2.csv")
    result = set()
    # , open(destination, "w+") as d
    with open(file, "r") as f:
        for line in f.readlines():
            one_line = [ln for ln in line.split(sep=" ") if len(ln) > 2]
            no_break = [w.strip() for w in one_line]
            fivers = {w.lower() for w in no_break if len(w) == cliargs.wordlength and w.isalpha()}
            result.update(fivers)
        # d.writelines(','.join(result))
        # d.write("\n")
    write_result(result)


def parse_cli_args() -> ArgsNamespace:
    nsp = ArgsNamespace()
    parser = argparse.ArgumentParser(
        prog="findfivers",
        description="find five-letter words in text, or other as parameter given")
    parser.add_argument("filename", help="the path to the file that contains the words "
                                         "where we find the five(or 'x')-letter long words",
                        default="lorem.txt", nargs="?", type=str)
    parser.add_argument("wordlength", help="the number of characters, the length of the word",
                        default=5, nargs="?", type=int)
    return parser.parse_args(namespace=nsp)


if __name__ == '__main__':
    args: ArgsNamespace = parse_cli_args()
    find_five(args)
