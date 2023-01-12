# import base64

import base64
# ff=open("dcomsmall.bin","rb")
# print(base64.b64encode(ff.read()))
# print("{0:08b}".format(3))
from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray
tempooor=open("testing_zip.zip","rb")
string_app=str((tempooor.read()).hex())
tempooor.close()
freq_lib = defaultdict(int)    # generate a default library
for ch in string_app:                # count each letter and record into the frequency library 
    freq_lib[ch] += 1
    
print(freq_lib)
heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]  # '' is for entering the huffman code later
print(heap)
heapify(heap) # transform the list into a heap tree structure
print(heap)
while len(heap) > 1:
    right = heappop(heap)  # heappop - Pop and return the smallest item from the heap
    print('right = ', right)
    left = heappop(heap)
    print('left = ', left)

    for pair in right[1:]:  
        pair[1] = '0' + pair[1]   # add zero to all the right note
    for pair in left[1:]:  
        pair[1] = '1' + pair[1]   # add one to all the left note
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])
huffman_list = right[1:] + left[1:]
# print(huffman_list)
huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)
writing_data=bitarray()
writing_data.encode(huffman_dict,string_app)
writing_data.append(0)
print(len(writing_data)%8)
dd=open("Comoressed.bin","wb")
dd.write(writing_data)
dd.close()