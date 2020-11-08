
min = 33
max = 122

MAX = max - 32

cipher = "<,$A]D/\"'6"
plaintext = "cheesecake"

cipherlist = [ord(c)-min for c in cipher]
plaintextlist = [ord(c)-min for c in plaintext]



print(cipherlist)
print(plaintextlist)    

keylist = []

for i in range(len(cipherlist)):
    if cipherlist[i] < plaintextlist[i]:
        keylist.append( MAX - (plaintextlist[i] - cipherlist[i]) )
    else:
        keylist.append(plaintextlist[i] - cipherlist[i])


print(keylist)

keylistfinal = ''.join( chr(c+32) for c in keylist )

print(keylistfinal)