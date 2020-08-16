m=int(input())
n=int(input())
lst1=[]
lst2=[]
for _ in range(m):
  lst1.append(input())
for _ in range(n):
  lst2.append(input())
print("Length of First List",len(lst1))
print("Length of Second",len(lst2))
print("First List Data")
for i in lst1:
    print(i)
print("Second List Data")
for i in lst2:
  print(i)
            