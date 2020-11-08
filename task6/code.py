import numpy as np

# Hamming code parity check matrix
parity_check = np.array([
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
])

# Dict to look up single-bit array errors
syndrome = {
    "11001": 0,
    "10011": 1,
    "01011": 2,
    "10110": 3,
    "01101": 4,
    "11111": 5,
    "11100": 6,
    "11010": 7,
    "10101": 8,
    "00111": 9,
    "01110": 10,
    "10000": 11,
    "01000": 12,
    "00100": 13,
    "00010": 14,
    "00001": 15
}

# Use 
# if all rows of result == 0, then it's a valid key
def paritycheck(word):
    b = np.array(word)
    result = np.mod(parity_check.dot(b), 2)
    if np.count_nonzero(result):
        try:
            index = syndrome[''.join([str(x) for x in result])]
        except KeyError: #Keyerrors will be thrown but aren't a huge deal
            print("KeyError found")
            print(result)
            print(word)
            print("")
            return word
        if word[index] == 1:
            word[index] = 0
        else: 
            word[index] = 1

    return word
            


data = ""

with open("signal.ham", "rb") as f:
    data = f.read()
    # a.frombytes(f.read(2))

datafloat = np.frombuffer(data, dtype=np.float16)

binary = []
for d in datafloat:
    if d > 0:
        binary.append(1)
    else:
        binary.append(0)

del data
del datafloat

n = 17
words = [binary[i * n:(i + 1) * n] for i in range((len(binary) + n - 1) // n )]

del binary

t = []
for w in words:
    t.append(paritycheck(w))

bits = [x[0:11] for x in t]
# parity = [x[11:17] for x in t]

data = ""
for b in bits:
    data = data + (''.join(str(x) for x in b))

n = 8
temp = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]

final = b''
for b in temp:
    final = final + bytes([int(b, 2)])

with open("output.avi", "wb") as f:
	f.write(final)

# length = 9600988
# Probably in 17 bit chunks, every 17th position is padded with 0 (generally)
# binary[16::17]


# 11 data, 5 parity, 1 padding at the end
