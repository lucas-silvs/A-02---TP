n=int(input())
for i in range(n):
    f=0
    d=input()
    if(d[0]==d[2]):
        f=int(d[0])*int(d[2])
    elif d[1].islower()==False:
        f=int(d[2])-int(d[0])
    elif d[1].islower()==True:
        f=int(d[0])+int(d[2])
    print(f)

