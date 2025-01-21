t = int(input())
while t>0:
  n, a, b, c = map(int,input().split())
  s = n//(a+b+c)*3
  n -= ((a+b+c)*s/3)
  if n>0:
    s+=1
    n-=a
    if n>0:
      s+=1
      n-=b
      if n>0:
        s+=1
  print(s)
  t-=1