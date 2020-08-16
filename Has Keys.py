dicti={}
n=int(input())
lst1=[]
lst2=[]
for _ in range(n):
  lst1.append(int(input()))
for _ in range(n):
  lst2.append(int(input()))
for i in range(n):
  dicti[lst1[i]]=lst2[i] 
s=int(input())
x=False
for i in dicti.keys():
  if i==s:
    x=True
print("The dictionary is")
print(dicti)
print(x)