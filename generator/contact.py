from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 1
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", email="", email2="", email3="",
                    homephone="", mobilephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("midlename", 20),
            lastname=random_string("lastname", 10), nickname=random_string("NickName", 8),
    email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("emails", 20),
            homephone=random_string("home", 20), mobilephone=random_string("mobile", 20), workphone=random_string("work", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))