s=str(input())
lst=[]
for i in s:
  lst.append(i)
t=lst[0]
lst[0]=lst[-1]
lst[-1]=t
print(''.join(lst))