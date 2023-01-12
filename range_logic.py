import base64
import datetime
zip_file=open("testing_tar.tar","rb")
print("after reading",datetime.datetime.now())
data=list(str(base64.b64encode(zip_file.read())))
ff=[]
print("after base 64",datetime.datetime.now())
sd=open("just_checking.tar","wb")
for i in data:
    ff.append(chr(ord(i)))
strrr="".join(map(str,ff))
# ss=""
# for i in ff:
#     ss+=i
zip_file.seek(0)
print(type(base64.b64encode(zip_file.read())))
print()
print()
print()
print()
print((bytes(strrr[2:len(strrr)-1],"utf8")))
print()
sd.write(base64.b64decode(bytes(strrr[2:len(strrr)-1],"utf8")))
sd.close()
zip_file.close()
print("finished",datetime.datetime.now())

