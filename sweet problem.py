t = int (input())

for i in range(t):
  a,b,c= map(int ,input().split())

  max_value =sorted([a,b,c])[1]+1
  print(min(max_value,a+b+c))
