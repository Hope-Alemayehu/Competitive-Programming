s,n=input().split()
n= int(n)

dragons=[]
for i in range(n):
  
  dragons.append(input().split())

dragons.sort(key=lambda x:x[0])

for dragon in dragons:
  if s>=dragon[0]:
    s+=int(dragon[1])
  else:
    print("No")
    break
else:
  print("YES")
