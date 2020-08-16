n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))
summ=0
for i in lst:
  if i>0 and i%2==0:
    summ+=i
print("Sum of positive even numbers:",summ)
