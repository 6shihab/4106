# Huffman Coding in python
# here dictionary is used
# Creating tree nodes

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(tree_object, left=True, binString=''):
    # print("tree start")
    # print(left)
    if type(tree_object) is str:
        # print(node, binString)
        return {tree_object: binString}  # returning dictionary

    (l, r) = tree_object.children()
    # print(l,r)
    d = dict()  # creating dictionary explicitly using dict() method
    d.update(huffman_code_tree(l, True, binString + '0'))  # updating the dictionary
    d.update(huffman_code_tree(r, False, binString + '1'))
    # print(d)
    # print("Tree end")0
    return d


string = 'AABC'

# Calculating frequency
freq = {}
print(type(freq))
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# next implementing priority queue
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)  # descending order
# print(type(freq))
# print(freq)
nodes = freq
# print(type(nodes))
print(nodes)

# processing the huffman tree from the string
if len(nodes) == 1:
    print(f"{string} --> 1")
else:
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]  # negative index to count from opposite direction
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        print(nodes)
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))  # adding a dictionary entry
        # print(nodes)
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        # print(nodes)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

print(huffmanCode)
