from math import sqrt


def primo(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def principal(numero):
    val = []
    for n in range(1, numero):
        if primo(n):
            val.append(n)
    return val
