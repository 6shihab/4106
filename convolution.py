# convu
def pos(x):
    p = []
    for i in range(0, len(x)):
        if x[i] == '1':
            p.append(i)
    return p


def multi(a, b):
    result = []
    a = [i for i in a]
    b = [i for i in b]
    a = pos(a)
    b = pos(b)
    for i in a:
        for j in b:
            if i + j not in result:
                result.append(i + j)
            else:
                result.remove(i + j)
    return result


g1 = "111"
g2 = "101"
m = "1001111"
print('G1= ', g1)
print('G2= ', g2)
print('Message= ', m)
c1 = multi(g1, m)
print(c1)
c2 = multi(g2, m)
print(c2)
max_num = max(max(c1), max(c2))
code = []
for i in range(0, max_num + 1):
    if i in c1:
        j = "1"
    else:
        j = "0"
    if i in c2:
        k = "1"
    else:
        k = "0"
    code.append(j + k)
print('Code: ', code)
