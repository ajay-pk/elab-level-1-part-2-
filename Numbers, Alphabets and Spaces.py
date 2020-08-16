s=str(input())
count1=0
count2=0
count3=0
for i in s:
  if i.isalpha():
    count2+=1
  elif i.isdigit():
    count1+=1
  elif i.isspace():
    count3+=1
print(count1)
print(count2)
print(count3)
