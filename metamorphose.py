import argparse

from lib.core import Core


def start() -> None:
    parser = argparse.ArgumentParser(prog="metamophose",
                                usage="%(prog)s [options]", 
                                description="metamorphose is used to insert flat file data to sqlite3 database file.",
                                epilog=f"This is still in development, So if you find any bug please report at {Core.email()}")
    parser.add_argument('-v', '--version', help="application version.")
    # parser.add_argument('f', help="input file.")
    args = parser.parse_args()


if __name__ == '__main__':
    Core.banner()
    start()