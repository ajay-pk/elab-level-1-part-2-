lst=[]
from itertools import permutations 
for _ in range(3):
  lst.append(input())
perm = permutations(lst) 
  

for i in list(perm): 
    print(*i)