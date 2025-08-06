import random
from hashlib import sha256
from json import loads

filename = str(input("enter snapshot filename: "))
print(filename)
file_text = open(filename).read()
random.seed(file_text)
print(random.choice(loads(file_text))["stake_addr"])
