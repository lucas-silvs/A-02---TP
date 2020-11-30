t=int(input())

for i in range(t):
    texto1,texto2=input().split()
    n=len(texto1)-len(texto2)
    aux=0
    final=0
   
    while n<len(texto1):
        
        if(texto1[n]== texto2[aux]):
            final+=1
            aux+=1
        n+=1
    
    if(final==len(texto2)):
        print("encaixa")
    else:
        print("nao encaixa")
    aux=0
    final=0
    n=0



