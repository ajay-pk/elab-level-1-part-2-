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
k=int(input())
print("The dictionary is")
print(dicti)
print(dicti[k])