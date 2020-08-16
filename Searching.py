n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))
s=int(input())
lst.sort()
c=0
for i in range(n):
  if s==lst[i]:
    print(s,"found at location",i+1)
    c=1
    break
if c==0:
  print(s,"not found")
    