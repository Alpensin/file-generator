import string
from random import choice


def pass_generate(passqnty=1, passminlen=8):
    return list(
        "".join(choice(string.printable[:63]) for j in range(passminlen))
        for i in range(passqnty)
    )
