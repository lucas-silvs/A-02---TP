t= int(input())
for i in range(t):
    texto=input()
    ts1=int(len(texto)/2)
    t1=""
    t2=""
    ts2=ts1-1
    sec=int(len(texto))-1
    while ts2>=0:
        t1=t1+texto[ts2]
        ts2-=1
    
    ts2=int(len(texto)/2)-1
    while sec>ts2:
        t2=t2+texto[sec]
        sec-=1
    
    final=t1+t2
    print(final)
