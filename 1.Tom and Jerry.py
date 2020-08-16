n=int(input())
lst=[]
lst_odd=[]
lst_even=[]
for _ in range(n):
  lst.append(int(input()))
for i in lst:
  if i%2==0:
    lst_even.append(i)
  else:
    lst_odd.append(i)
print(lst_even)
print(lst_odd)