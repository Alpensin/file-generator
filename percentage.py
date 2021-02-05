import sys


def percentage(base, c, r=False):
    if r is not False:
        return 100 - 100 * c / base
    return 100 * c / base


if __name__ == "__main__":
    if len(sys.argv) == 3:
        base, c = map(int, sys.argv[1:])
        print(percentage(base, c))

    elif len(sys.argv) == 4:
        base, c = map(int, sys.argv[1:3])
        r = sys.argv[3]
        print(percentage(base, c, r))

    else:
        print("введено неверное количество аргументов")
