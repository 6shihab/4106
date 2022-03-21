from heapq import heapify, heappop, heappush
from collections import defaultdict

message = "HappyHappy"

frequency = defaultdict(int)
for ch in message:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# frequency.pop(' ')

for ch in frequency:
    print(ch, frequency[ch])

heap = [[freq, [symbol, ""]] for symbol, freq in frequency.items()]
for ch in heap:
    print(ch)


heapify(heap)
for ch in heap:
    print(ch)

print("   ")


while len(heap) > 1:
    right = heappop(heap)
    left = heappop(heap)
    for pair in right[1:]:
        pair[1] = '0' + pair[1]
    for pair in left[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])

print("heap after operation:", heap)

code = []
for ch in heap:
    for c in ch:
        code.append(c)

print(code)

code = code[1:]
print('Code: ', code)

bit = ''
for ch in message:
    for c in code:
        if ch == c[0]:
            bit = bit + c[1]
            break
print('code: ', bit)

decode = ''
c = ""
for b in bit:
    c = c + b
    for co in code:
        if c == co[1]:
            decode = decode + co[0]
            c = ''
            break

print('decode: ', decode)
