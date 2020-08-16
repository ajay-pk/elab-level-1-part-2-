n=int(input())
lst=list(map(int,input().split()))
s=int(input())
import math
lst_fact=[]
for i in lst:
  lst_fact.append(math.factorial(i))
c=0
for i in range(n):
  if s==lst_fact[i]:
    print(lst[i])
    c=1
    break
if c==0:
  print("Not found")
    