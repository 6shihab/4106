import math

n = 7
str = [" "]*7
msg = [1, 1, 0, 1]
p = n - len(msg)
possibility = False

if math.pow(2, p) >= p+1+len(msg):
    possibility = True
else:
    print("This configuration is not possible")

parity_index = []
for i in range(0, p):
    parity_index.append(int(7 - math.pow(2, i)))

parity_index.sort(reverse=True)
print(parity_index)

#putting msg bits in the empty string list
for i in range(0, len(msg)):
    if i not in parity_index:
        str[i] = msg[i]
    else:
        str[i+1] = msg[i]

print(str)


def xor_three(a, b, c):
    d = a ^ b
    return d ^ c


def parity_generator(list):
    parity_list = []
    p1 = xor_three(list[4], list[2], list[0])
    p2 = xor_three(list[4], list[1], list[0])
    p3 = xor_three(list[2], list[1], list[0])
    parity_list.append(p1)
    parity_list.append(p2)
    parity_list.append(p3)
    return parity_list


parity_bits = parity_generator(str)

print(parity_bits)


#putting msg bits in the empty string list
for i in range(0, len(parity_bits)):
    str[parity_index[i]] = parity_bits[i]

print(str)

error_msg = [1, 0, 1, 1, 0, 1, 0]
print(error_msg)


def received_parity(List):
    received_parity_list = []
    for i in range(0, len(parity_index)):
        received_parity_list.append(List[parity_index[i]])

    return received_parity_list


received_parity1 = received_parity(error_msg)

calculated_received_parity = parity_generator(error_msg)

print("Received Parity -> ", received_parity1)
print("calculated parity ->", calculated_received_parity)


def error_position(List1, List2):
    Reference = [1, 2, 4]
    flag = []
    for i in range(0, len(List1)):
        if List1[i] == List2[i]:
            flag.append(0)
        else:
            flag.append(Reference[i])

    return 7-sum(flag)


error_index = error_position(received_parity1, calculated_received_parity)

print("error at index -> ",error_index)


def error_correction(x, List):
    List1 = [0]*n
    List1[x] = 1
    corrected = []
    for i in range(0, len(List)):
        corrected.append(List[i] ^ List1[i])

    return corrected


correct = error_correction(error_index, error_msg)

print("Corrected Msg - > ", correct)
print("original Msg  - > ", str)









