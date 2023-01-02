# # import numpy as np
# # sss=""
# # ff=open("binary_file.txt","wb")
# # charmap_dic={}
# # key_cjarmap=0
# # for indec_cgmao in range(0,68538,1):
# #     if indec_cgmao<55296 or indec_cgmao>58296:
# #         charmap_dic[key_cjarmap]=chr(indec_cgmao)
# #         key_cjarmap+=1
# # # print(key_cjarmap)
# # string_arr=[]
# # for i in range(65537):
# #     string_arr.append(i)
# # string_arr=np.asarray(string_arr)
# # string_arr=np.vectorize(charmap_dic.get)(string_arr) 
# # on=0
# # for i in charmap_dic:
# #     if not charmap_dic[i].isalpha():
# #         on+=1
# # print("NOnes",on)
# # # ff.write(str(charmap_dic).encode("utf8"))
# # ff.close()

# # # ff=open("binary_file.txt","r")
# # # dss=ff.read()
# # # print(len(dss))

# # ff.close()
# # # 55296
# # from typing import Counter
# # import numpy as np
# # dic={}
# # for i in range(68538):
# # 	if i<55296 or i>58296:
# #                 dic[i]=chr(i)
# # ff=open("ff.txt","wb")
# # for i in range(32768):
# #     string_arr=np.vectorize(dic.get)(i) 
# #     # ff.write(str(string_arr).encode("utf8"))
# #     if string_arr=="None":
# #         print(i)
# # print(ord("翿"))
# from collections import Counter

# sss=[]
# for i in range(12898,29282,1):
#     sss.append(chr(i))
# sss=dict(Counter(sss))
# f=0
# for i in sss:
#     if sss[i]!=1:
#         print(i)
#     else:
#         f+=1
# print(f)
# print(len(sss))

# # print(type(dict(sss)))


import base64
import enum
from ftplib import ftpcp
from pickle import bytes_types
import shutil
# import textract
import os 
import hashlib
archived = shutil.make_archive('ert', 'zip', 'F:/testinggit/datas')
f1=open("ert.zip","rb")
# print(bytes.fromhex(f1.read().hex()))
# fgt=hashlib.sha256(f1.read()).hexdigest()
print(f1.read())
f2=open("createdzip.zip","wb")
f1.seek(0)
# f2.write(bytes.fromhex(f1.read().hex()))
f2.write(base64.b64decode(base64.b64encode(f1.read())))
f1.close()
f2.close()
shutil.unpack_archive("createdzip.zip")
os.remove("createdzip.zip")

# text=textract.process(r"F:\testinggit\datas\The.Amazing.Spiderman.(2012).1080p.Dual.Audio.(Hin-Eng)-001.mkv",encoding="utf-8")
# print(text)
# ff=open(r"F:\testinggit\datas\amzing_movie.mkv","rb")
# ff_byte=ff.read()
# ff.close()
# ff=open("dscds.txt","wb")
# ff.write(ff_byte)
# print(ff_byte)
# ff.close()
# ss="sdadas"
# for id,i in enumerate(ss):
#     print(id)