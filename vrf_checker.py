import random
from json import loads

file_text = open(str(input("enter snapshot filename: "))).read()
random.seed(file_text)
print(random.choice(loads(file_text))["stake_addr"])
