n=int(input())
ans=-1
c=n
count=0

while True:
    a = c//10
    b = c%10
    
    num = a+b
    b2 = num%10
    
    ans = b*10 + b2
    count +=1
    if n==ans:
        break
    c=ans
    
print(count)

