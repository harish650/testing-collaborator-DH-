import base64
import heapq
import datetime
import sys
import time
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
	charmap_dic={}
	key_cjarmap=0
	for indec_cgmao in range(12898,29282,1):
			charmap_dic[key_cjarmap]=chr(indec_cgmao)
			key_cjarmap+=1
	f=open("testing_zip.zip","rb")
	# str1=f.read()	


	print("aftering reading a file:",datetime.datetime.now())
	# .translate({ord(c): None for c in string.whitespace})
	# print(len(string))
	final_dic_list=[]
	rrun=0
	old_len=0
	while True:
		dic={}
		tempooor=open("dcomsmall.txt","rb")

		if rrun==0:
			unique=Counter(list(str(base64.b64encode(f.read()))))
			f.seek(0)
			print("file sze:",len(f.read()))
			print("unique element size :",len(unique))
			print(unique)

		else:
			unique=Counter(list(tempooor.read().decode("utf8")))

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
		print(dic)
		print("after heap:",datetime.datetime.now())
		if rrun==0:
			f.seek(0)
			string_arr=np.asarray(list(str(base64.b64encode(f.read()))))
		else:
			tempooor.seek(0)
			string_arr=np.asarray(list(tempooor.read().decode("utf8")))
		tempooor.close()

		string_arr=np.vectorize(dic.get)(string_arr) 
		# temp_string_arr=""
		# for stringngg in string_arr:
			# temp_string_arr+=dic[stringngg]
		# string_arr=temp_string_arr
		# tempstr=""

		dd=open("dcomsmall.txt","wb")
		dd.seek(0)
		print("started multi ",datetime.datetime.now())
		flag=0
		try:
			# for i in string_arr:
			# 	tempstr+=i
			# 	if len(tempstr)>=8:
			# 		dd.write(chr(int(tempstr[0:8],2)).encode("utf8"))
			# 		tempstr=tempstr[8:len(tempstr)+1]
			# dd.write(chr(int(tempstr,2)).encode("utf8"))
			# dd.write(str(len(tempstr)).encode("utf8"))
			with Manager() as manager:
				queue=multiprocessing.Queue()
				p1 = Process(target=fun, args=(string_arr,queue))
				p1.start()
				print("process")
				while True:  
					l1=queue.get()
					if l1=="e":
						break
					else:
						if l1[len(l1)-1]=="e":
							if len(l1)==3:
								last_value_of_every_file=" "+l1[:2]
								dd.write(last_value_of_every_file.encode("utf8"))
								# print(l1[0])
								break
							else:
								last_value_of_every_file=" "+l1[:1]
								dd.write(last_value_of_every_file.encode("utf8"))
								# print(l1[0])
								break
						else:
							# new_li=""
							# if len(l1)!=0:
								# if l1.isdigit():
									# dd.write(chr(int(l1,2)).encode("utf8"))
								# else:
									# for i in str(l1):
										# if i.isdigit():	
											# new_li+=i
									# dd.write(chr(int(new_li,2)).encode("utf8"))
							# 		print(new_li)
							# if not l1.isdigit():

							dd.write(charmap_dic[int(l1,2)].encode("utf8"))

				p1.join()
				# dd.write(str(dic).encode("utf8"))  main think adding dic to last of the file..
				dd.close()
				print("after while")
		except Exception as e:
			print(e)
			dd.close()
		if rrun ==0:
			f.close()


		dd=open("dcomsmall.txt","rb")
		if rrun!=0:
			dd.seek(0)
			if len(dd.read().decode("utf8"))+len(str(final_dic_list))<old_len:
				dd.seek(0)
				old_len=len(dd.read().decode("utf8"))+len(str(final_dic_list))
				dd.close()
			else:
				dd.close()
				break
		else:
			dd.seek(0)
			old_len=len(dd.read().decode("utf8"))+len(str(final_dic_list))	
			dd.close()
		rrun+=1
		print(old_len)
	print("after writing into file decom:",datetime.datetime.now())
	dd=open("dcomsmall.txt","ab")
	dd.write(str(final_dic_list).encode("utf8"))
	dd.close()
	print("finished")
	print(rrun)

