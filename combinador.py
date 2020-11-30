t=int(input())

for i in range(t):
    p,t=input().split()
    final=""
    
    if(len(p)>len(t)):
        aux=0
        for i in range(len(t)):
            
            final=final+p[i]
            final=final+t[i]
            aux=aux+1
        while(aux<len(p)):
            final=final+ p[aux]
            aux=aux+1
    
    elif(len(p)<=len(t)):
        aux=0
        for i in range(len(p)):
            final=final+p[i]
            final=final+t[i]
            aux=aux+1
        while(aux<len(t)):
            final=final+ t[aux]
            aux=aux+1
        
    print(final)
            
    