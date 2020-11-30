
while True:
    nnum,ncort= input().split()
    if nnum=="0" and ncort=="0":
        break
    num=list(input())
    aux=0
    while aux<int(ncort):
        for i in range(len(num)):
            if(i<len(num)-1 and num[i]>num[i+1]):
                del num[i+1]
                aux+=1
            elif(i<len(num)-1 and num[i]<num[i+1]):
                del num[i]
                aux+=1
    print(num)
    #print(num.index("2"))













    
