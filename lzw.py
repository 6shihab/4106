data = '000101110010100101'
data = [i for i in data]
code = ""
code_l = []
print(data)
for i in data:
    if i not in code_l:
        code_l.append(i)

l = len(code_l)

for i in data:
    code = code + i
    if code not in code_l:
        code_l.append(code)
        code = ""

output = []

for i in range(l, len(code_l)):
    word = code_l[i]
    lastBitOfWord = word[-1]
    firstBitsOfWord = word[:-1]
    index1 = 1 + code_l.index(firstBitsOfWord)  # adding with 1 because it is 0 based index
    index_bin = format(index1, 'b')  # turning it into binary
    output.append(str(index_bin) + lastBitOfWord)
print('Different symbol: ', code_l)
print('Code: ', output)
