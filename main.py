import random as r
import string


def a(b):
    for i in range(0, b):
        if i % 2 == 0:
            print("Je sais coder en python pour la " + str(i) + " eme fois :)")
        else:
            print("Oupsi " + str(i) + " est un nombre impair.")


def gen_lettre():
    return r.choice(string.ascii_letters)


def gen_chiffre():
    return r.randint(0, 9)


def gen_chiffre_ou_lettre():
    """
    On génère aléatoirement une lettre ou un chiffre. Il y a 52 lettres et 10 chiffres. Pour que chaque caractère ait
    autant de chances d'apparaître, j'ai donné 52 chances pour les lettres et 10 chances pour les chiffres.
    """
    if r.randint(0, 62) < 52:
        return gen_lettre()
    return str(gen_chiffre())


def gen_nounce(x):
    return ''.join(gen_chiffre_ou_lettre() for _ in range(0, x))


"""def gen_nounce():
    return ''.join(gen_chiffre_lettre() for _ in range(0, 4))"""

print(gen_nounce(20))
