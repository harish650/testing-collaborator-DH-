#receiving back
import base64
import time
import multiprocessing 
# from multiprocessing import Process, Manager

def decodecode(dstring,queue,charmap_dic):
    # end=0
    # while True:
        # print("fun")
        # 
        
        f=0
        last_ele_sze=0
        three_or_two=0
        if dstring[len(dstring)-1].isdigit():
            if dstring[len(dstring)-2].isdigit():
                last_ele_sze=dstring[len(dstring)-2]+dstring[len(dstring)-1] 
                three_or_two=4
            else:
                last_ele_sze=dstring[len(dstring)-1]
                three_or_two=3
            for i in dstring:
                if len(dstring)>f+three_or_two:
                    queue.put('{:014b}'.format(charmap_dic[i]))
                    f+=1
                elif len(dstring)==f+three_or_two:        
                    nnn='{:0'+last_ele_sze+'b}'
                    queue.put(nnn.format(charmap_dic[i]))
                    f+=1
            else:
                end=1
                queue.put("e")
        else:
            for i in dstring:
                queue.put('{:014b}'.format(charmap_dic[i]))
            else:
                end=1
                queue.put("e")
        # if end==1:
        #     break
    
if __name__ == '__main__':
    multiprocessing.freeze_support()
    t=time.time()
    print("starting decode ",t)
    charmap_dic={}
    key_cjarmap=0
    for indec_cgmao in range(12898,29282,1):
            charmap_dic[chr(indec_cgmao)]=key_cjarmap
            key_cjarmap+=1
    dd=open("dcomsmall.txt","rb")
    
    dstring=dd.read().decode("utf8")
    sss=0
    for id in range(len(dstring)-2,0,-1):

        if dstring[id]=="[" and dstring[id+1]=="{":
            sss=id
            break
        

    dic=dstring[sss:]
    dic=list(eval(dic))
    print(len(dic))
    dstring=dstring[:sss]
    for iddd,dic_id in enumerate(dic):
        my_dict2 = {y: x for x, y in dic[len(dic)-iddd-1].items()}
        key=my_dict2.keys()
        if iddd==0:
            od=open("after_com_orinal.txt","wb")
        else:
            od=open("after_com_orinal.txt","rb")
            dstring=od.read().decode("utf8")
            od.close()
            od=open("after_com_orinal.txt","wb")
        jhd=""
        tt=""
        breaking=0
       
        with multiprocessing.Manager() as manager:
                queue=multiprocessing.Queue()
                p1 = multiprocessing.Process(target=decodecode, args=(dstring,queue,charmap_dic))
                # print("strted multi")
                p1.start()
                fg=0

                while True:
                    if fg==0:
                        tt=queue.get()
                    if tt=="e":
                        fg=1
                    else:
                        jhd+=tt

                    j=1
                    while True:                   
                        if jhd[:j] in key:
                            od.write(my_dict2[jhd[:j]].encode("utf8"))
                            jhd=jhd[j:]
                            break
                        elif j==len(jhd):
                            break
                        elif len(jhd)==0:
                            break
                        else:
                            j+=1
                    # print(jhd)  
                    if tt=="e" and len(jhd)==0:
                        break
                p1.join()

                od.close()
                if iddd==0:
                    dd.close()
                print("end decode ",time.time()-t)
    print('ended ',time.time()-t)
    dfdfS=open("after_com_orinal.txt","rb")
    ert=open("AFTER_com_orinal.zip","wb")
    sdf=bytes(dfdfS.read())
    ert.write(base64.b64decode(sdf[2:]))
    ert.close()
    dfdfS.close()
