import random as r
import string
import hashlib
import time


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


def proof_of_work(difficulte: int, transactions: str, last_hash: str):
    count = 0
    start_time = time.time()
    while 1:
        count += 1
        nounce = gen_nounce(64)
        block = transactions + last_hash + nounce
        block = bytes(block, 'utf-8')
        bon = True
        varhash = hashlib.sha224(block).hexdigest()
        for i in range(0, difficulte):
            if varhash[i] != "0":
                bon = False
        if bon:
            print("nombre d'essais avant de trouver : " + str(count))
            print("hash obtenu : " + varhash)
            print("durée d'execution : " + str(time.time() - start_time))
            return nounce


print(proof_of_work(16, "test", "2g6f5fz6dfsdf5e4fz6"))
