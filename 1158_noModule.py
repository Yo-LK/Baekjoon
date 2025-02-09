n,k=map(int,input('').split())
b=0
count=0

l=[]
l2=[]

for i in range(n):
    l.append(i+1)
    

while not count==n:
    for p in range(k-1):
        b=l.pop(0)           # pop()의 기본은 제일 뒤에 적용됨
        l.append(b) 
        
    a=l.pop(0)
    l2.append(a)
    count+=1

print('<'+ ', '.join(map(str, l2))+'>')
