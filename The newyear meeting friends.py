x1,x2,x3 =input().split()
x1,x2,x3=sorted([int (x1),int(x2),int (x3)])


distance1=abs(x1-x2)+abs(x2-x3)
distance2= abs(x1-x3)+abs(x3-x2)
distance3=abs(x2-x1)+abs(x2-x3)

min_distance =min(distance1,distance2,distance3)
print(min_distance)
