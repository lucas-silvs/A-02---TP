t = int(input())
l=[]
for i in range(t):
   
    l.append(int(input()))
    l.sort()
j=0


freq=dict()
while(j<len(l)):
        
        n=l.count(l[j])
        if(l[j] not in freq):
            freq[l[j]]=n

        j+=1
    

for i, j in freq.items():
    print("%d aparece %d vez(es)"%(i,j))