import base64
import heapq
import datetime
import sys
import time
from bitarray import bitarray
from collections import Counter
import numpy as np
from multiprocessing import Process, Manager
import multiprocessing
class node: 
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''		
    def __lt__(self, nxt):
        return self.freq < nxt.freq
        
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):
        # print(f"{node.symbol} -> {newVal}")
        dic[node.symbol]=newVal

def fun(sample,queue):
    temp=""
    si=0
    n=len(sample)-1
    temp+=sample[si]
    while True:
        
        if len(temp)>=14:
            
            queue.put(temp[0:14])
            temp=temp[14:len(temp)]
        if si==n:
            if len(temp)==0:
                queue.put("e")
                break
            elif len(temp)<14:
                queue.put(temp[0:len(temp)])
                tr=str(len(temp))+"e"
                queue.put(tr)
                break
        else:
            si=si+1
            temp+=sample[si]
if __name__ == '__main__':
    multiprocessing.freeze_support()

    print("start:",datetime.datetime.now())
    f=open("testing_zip.zip","rb")
    print("aftering reading a file:",datetime.datetime.now())
    final_dic_list=[]
    rrun=0
    while True:
        dic={}

        if rrun==0:
            unique=Counter(list(str(base64.b64encode(f.read()))))
            # unique=Counter(list((f.read())))
            list=[]
            for i in unique:
                list.append(i)
            print(list)
            print(len(list))
            f.seek(0)
            string_app=(str(base64.b64encode(f.read())))
            # string_app=f.read()
            # print("STRING_APP",string_app)
            print("DATA LENGTH",len(string_app))
            print("DATA SIZE",sys.getsizeof(string_app))
            f.close()
        else:
            tempooor=open("dcomsmall.bin","rb")
            unique=Counter(list(str(base64.b64encode(tempooor.read()))))
            tempooor.seek(0)
            string_app=str(base64.b64encode(tempooor.read()))
            # print("STRING_APP",string_app)
            print("DATA LENGTH",len(string_app))
            print("DATA SIZE",sys.getsizeof(string_app))
            tempooor.close()

        nodes=[]
        print("after unique element :",datetime.datetime.now())
        for x in unique:
            heapq.heappush(nodes, node(unique[x], x))
        while len(nodes) > 1:	
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            left.huff = 0
            right.huff = 1
            newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
            heapq.heappush(nodes, newNode)

        printNodes(nodes[0])
        final_dic_list.append(dic)
        
        print("after heap:",datetime.datetime.now())
        with open("dcomsmall.bin","wb") as dd:
            writing_data=bitarray()
            
            dic={a:bitarray(str(dic[a])) for a in dic}
            writing_data.encode(dic,string_app)
            # print(sys.getsizeof(writing_data))
            # print("WRITING DATA ",writing_data)
            print("WRITING DATA LENGTH",len(writing_data))
            extra_padding=0
            if len(writing_data)%8!=0:
                for i in range(8-len(writing_data)%8):
                    writing_data.append(0)
            front_extra_padding="{0:08b}".format(extra_padding)
            for i in range(len(front_extra_padding)):
                writing_data.insert(0,int(front_extra_padding[len(front_extra_padding)-i-1]))
            print("WRITING DATA LENGTH",len(writing_data))
            print("WRITING DATA SIZE",sys.getsizeof(writing_data))
            dd.write(bytes(writing_data))
            # strr=str(writing_data)
            # string_app=strr[10:len(strr)-2]
            # extra_padding=0
            # if len(string_app)%8!=0:
            #    extra_padding=8-len(string_app)%8
            #    for i in range(extra_padding):
            #        string_app+="0"
            # print("dadasf",len(string_app)%8)
            # string_app="{0:08b}".format(extra_padding)+string_app
            # print(len(string_app))
            # writing_data=bytearray()
            df=open("dcomsmall.txt","wb")
            # for i in range(0,len(string_app),8):
                # df.write(chr(int(string_app[i:i+8],2)).encode("utf8"))
                # writing_data+=(chr(int(string_app[i:i+14],2)))
            # dd.write(bytes(writing_data))
            # print("size",sys.getsizeof((writing_data)))
        dd.close()
        df.close()
        print("started multi ",datetime.datetime.now())
        if rrun==0:
            break
        rrun+=1
       

    print("after writing into file decom:",datetime.datetime.now())
    dd=open("dcomsmall.txt","ab")
    dd.write(str(final_dic_list).encode("utf-8"))
    dd.close()
    print("finished")
    print(rrun+1)

