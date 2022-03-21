def parity_generator(parity_pos, mess):
    k = 0
    x = []
    i = parity_pos
    # generating the parity
    # we will create the array x in such way that each parity is generated depending upon itz parity pos(neso academy solution)
    while i <= len(mess):
        print(i, k, x)
        if k < parity_pos:
            x.append(mess[i - 1])
            k = k + 1
        else:
            k = 0
            i = i + parity_pos - 1
        i = i + 1
    print(x)
    add = 0
    for j in x:
        if j != '?':
            add = add + int(j)
    if add%2:
        return 1
    else:
        return 0

# main code starts from here
parity_pos = []
#generating parity
for i in range(5):
    parity_pos.append(2**i)
print("parity position:", parity_pos)
mess = "1101"
mess = [i for i in mess]

print("message: ", mess)

# checking how many parity bits we need, for our program we need 3
for i in range(1,6):
    l = len(mess) + i
    if l <= parity_pos[i-1]:
        break
parity = i-1
print("we need parity ", parity)
# inserting ? mark in as parity in index 0, 1 and 3
for i in range(0, parity):
    mess.insert(parity_pos[i] - 1, '?')

print('Message with Parity position:' , mess)


for i in parity_pos:
    if i < len(mess):
        mess[i-1] = parity_generator(i, mess)
    else:
        break

print('Message with Parity position:', mess)
