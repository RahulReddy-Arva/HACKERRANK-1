k=int(input())
n=k-1
st=n*(n+1)//2+1
nost=1+(st-1)*2
ans=0
#print(nost)
while(k>0):
    k-=1
    ans+=nost
    nost+=2
print(ans)