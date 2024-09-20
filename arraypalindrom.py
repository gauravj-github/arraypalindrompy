arr = [1, 232, 5545455, 909090, 161]
l=[]

for i in arr:

    sum=0
    s=i
    while(s>0):
        temp=s%10
        sum=(sum*10)+temp
        s=s//10
    if sum in arr:
        l.append(sum)

print(l)
m=l[0]
for j in range(1,len(l)):
    if m<l[j]:
        m=l[j]
        l[j]=m
print(m)




            