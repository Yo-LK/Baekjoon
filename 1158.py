from collections import deque

n,k = map(int, input().split()) 
circle = deque(range(1, n + 1)) 
result = [] 

while circle:
    circle.rotate(-(k - 1)) 
    result.append(circle.popleft()) 

print('<' + ', '.join(map(str, result)) + '>')
