saida=False
while saida==False:
    
    frase=input().split()
    if(frase[0]=="*"):
        saida=True
        
    else:
        aux=0

        for i in range(len(frase)-1):
            if(frase[i][0].upper()==frase[i+1][0].upper()):
                aux=aux+1
            
        if(aux==len(frase)-1):
            print("Y")
            
        else:
            print("N")
