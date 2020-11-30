c=int(input())
num=[]
for i in range (c):
    num=[]
    leds=[]
    final=0

    num=list(input())
    #print(num)
    for j in range(len(num)):
        if num[j] == "0":
            final=final+6
        if num[j] == "1":
            final=final+2
        if num[j] == "2":
            final=final+5
        if num[j] == "3":
            final=final+5
        if num[j] == "4":
            final=final+4
        if num[j] == "5":
            final=final+5
        if num[j] == "6":
            final=final+6
        if num[j] == "7":
            final=final+3
        if num[j] == "8":
            final=final+7
        if num[j] == "9":
            final=final+6
    
    print(final,"leds")
        


    

    

        
