dict1={}
dict2={}
x=int(input())
dict1[x]=int(input())
y=int(input())
dict2[y]=int(input())
print("First Dictionary")
print(dict1)
print("Second Dictionary")
print(dict2)
print("Concatenated dictionary is")
dict3={}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)
print("Total sum of values in the dictionary")
print(sum(dict3.values()))
