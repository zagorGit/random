import string
import random
# string.ascii_letters string.digits string.printable
def passw(size=8, chars=string.ascii_lowercase + string.ascii_uppercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))
# string.printable - string.punctuation - string.whitespace
passwrd = []
for i in range (10000):
    passwrd.append(passw())

from random import choice
for i in range (10):
    print choice(passwrd)

"""
import random, string

digits = ''.join(random.sample(string.digits, 8))
chars = ''.join(random.sample(string.letters, 15))
"""

import random
for i in range (12):
    lotterynumbers = []
    x = 0

    while x < 7:
        a = random.randint(1, 39)
        if a not in lotterynumbers:
            lotterynumbers.append(a)
            x += 1

    lotterynumbers.sort()
    print lotterynumbers
