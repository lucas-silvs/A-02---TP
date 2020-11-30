n=int(input())
for i in range(n):
    frase=input().split()
    frase.sort(key=len, reverse=True)
    
    print(''.join(frase))
