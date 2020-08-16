n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))
s=int(input())
c=0
for i in lst:
  if i==s:
    c+=1
print(c)