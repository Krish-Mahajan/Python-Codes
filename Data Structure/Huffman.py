'''
Created on Nov 12, 2015

@author: Krish
'''
from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    print(heap)

    
    while len(heap) > 1:
        lo = heappop(heap)
        #print(lo[1:],lo[0],lo[1])
        hi = heappop(heap)
        #print(hi[1:],hi[0],hi[1])
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
            #print(pair[1])
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
            #print(pair[1])
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        print(heap)
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    
txt = "AAAbcd"
symb2freq = defaultdict(int)

for ch in txt:
    symb2freq[ch] += 1

print(symb2freq)    
# in Python 3.1+:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq)
print("Symbol\tWeight\tHuffman Code")
for p in huff:
    print("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))