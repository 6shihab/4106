def modulo(bits):
    bits = [int(i) for i in bits]
    return bits[0] ^ bits[1] ^ bits[2]


def parity_generator(message):
    parity_list = []
    p1 = modulo([message[3 - 1], message[5 - 1], message[7 - 1]])
    p2 = modulo([message[3 - 1], message[6 - 1], message[7 - 1]])
    p3 = modulo([message[5 - 1], message[6 - 1], message[7 - 1]])
    parity_list.append(p1)
    parity_list.append(p2)
    parity_list.append(p3)

    return parity_list


parity_pos = []

for i in range(3):
    parity_pos.append(2 ** i)
print("parity position:", parity_pos)
message = "1101"
message = [i for i in message]

print("message: ", message)

# inserting ? mark in as parity in index 0, 1 and 3
for i in range(3):
    message.insert(parity_pos[i] - 1, '?')

print('Message with Parity position:', message)
parity_bits = parity_generator(message)
print("Parity Bits:", parity_bits)
j = 0
for i in parity_pos:
    if i < len(message):
        message[i - 1] = parity_bits[j]
        j = j + 1
    else:
        break

print('Message with Parity position:', message)
