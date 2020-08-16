n=int(input())
lst=list(map(int,input().split()))
lst.sort()
incr_lst=[]
for i in range(n-1):
  x=i+1
  incr_lst.append(lst[x]-lst[i])
print("Sorted List")
print(lst)
print("Sequence of increments")
print(incr_lst)