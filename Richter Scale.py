x=float(input())
if x<2.0:
  print("Micro")
elif x>=2.0 and x<3.0:
  print("Very minor")
elif x>=3.0 and x<4.0:
  print("Minor")
elif x>=4.0 and x<5.0:
  print("Light")
elif x>=5.0 and x<6.0:
  print("Moderate")
elif x>=6.0 and x<7.0:
  print("Strong")
elif x>=7.0 and x<8.0:
  print("Major")

elif x>=8.0 and x<10.0:
  print("Great")
else:
  print("Meteoric")