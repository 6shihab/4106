import math
import matplotlib.pyplot as plt
import random

p = []
for i in range(10000):
    p.append(random.random())

p.sort()
print(p)
H = []

print("P:", p)

for i in p:
    h = -i * math.log(i, 2) - (1 - i) * math.log((1 - i), 2)
    H.append(h)

plt.plot(p, H)
plt.xlabel('p')
plt.ylabel('H(p)')
plt.show()
