from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for name in range(1)
]


