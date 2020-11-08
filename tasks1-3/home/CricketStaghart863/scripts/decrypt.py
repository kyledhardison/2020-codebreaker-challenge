
min = 32
max = 122

MIN = min - 32
MAX = max - 32


key = "b7s9j"
cipher = "9jr'\\"

cipherlist = [ord(c)-min for c in cipher]
keylist = [ord(c)-min for c in key]



print(cipherlist)
print(keylist)    

plaintextlist = []

for i in range(len(cipherlist)):
    if cipherlist[i] < keylist[i]:
        plaintextlist.append( MAX - (keylist[i] - cipherlist[i]) )
    else:
        plaintextlist.append( cipherlist[i] - keylist[i] )


print(plaintextlist)

plaintext = ''.join( chr(c+32) for c in plaintextlist )

print(plaintext)