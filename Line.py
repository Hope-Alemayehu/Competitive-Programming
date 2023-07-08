import math
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    if n==1:
        print(0)
        continue
    ac = []
 
    for i in range(n):
        if a[i]=='L':
            ac.append(i)
        else:
            ac.append(n-i-1)
    
    bal = [i for i in range(math.ceil(n/2),n)]
    per = []
    if n%2==0:
        per = bal[::-1] + bal
    else:
        per = bal[::-1] + [n//2] + bal
    
    acsum = sum(ac)
 
    b,c = [],[]
    for i in range(n):
        if ac[i]!=per[i]:
            b.append(ac[i])
            c.append(per[i])
    
    if len(b)==0:
        print(*[acsum]*n)
        continue
 
    b.sort()
    c.sort(reverse=True)
 
    preb = [b[0]]
    prec = [c[0]]
 
    for i in range(1,len(c)):
        preb.append(preb[i-1]+b[i])
        prec.append(prec[i-1]+c[i])
    
    ans = []
 
    for i in range(len(c)):
        ans.append(acsum-preb[i]+prec[i])
    
    ans += [ans[-1]]*(n-len(c))
    print(*ans)
