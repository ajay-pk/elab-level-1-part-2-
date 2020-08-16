n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))
s=int(input())
for i in range(n):
  if s==lst[i]:
    print("Element is present at index",i)
    