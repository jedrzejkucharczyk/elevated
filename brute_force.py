import random
import itertools
import os
#szyfrowanie
def cypher(string):
    chain = ''
    table = []
    for x in range(len(string)):
        salt = random.randint(32, 126)
        hider = ord(string[x]) + salt
        while hider > 126:
            hider = hider - 126 + 32
        table.append(salt)
        letter = chr(hider)
        chain = chain + letter
    return chain,table

#odszyfrowanie
def decode(string,salt):
    password = ''
    for x in range(len(string)):
        solver = ord(string[x]) - salt[x]
        password = password + chr(solver)
    return password

def brute(len):
    #Aby nie było problemu z pamiecia najlepiej wykonac polecenie w locie
    #with open("test.txt", "a") as myfile:
    #    [myfile.write("".join(item) + "\n") for item in itertools.product([chr(x) for x in range(32, 127)], repeat=len)]
    for item in itertools.product([chr(x) for x in range(32, 127)], repeat=len):
        brute_pass = "".join(item)