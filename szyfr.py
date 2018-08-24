import random
#szyfrowanie
def cypher(string):
    chain = ''
    table = []
    for x in range(len(string)):
        salt = random.randint(32, 65535)
        hider = ord(string[x]) + salt
        while hider > 65535:
            hider = hider - 65535
        table.append(salt)
        letter = chr(hider)
        chain = chain + letter
    chain2=''
    for x in table:
        chain2 = chain2 + chr(x)
    haslo=chain+chain2
    return haslo

#odszyfrowanie
def decode(string):
    password = ''
    chain = string[0:len(string)//2]
    chain2 = string[len(string)//2:len(string)]
    for x in range(len(chain)):
        solver = ord(chain[x]) - ord(chain2[x])
        password = password + chr(solver)
    return password