t = int(input())
while t:
    n = int(input())
    r=0
    while n:
        r+=1
        if not(r%3==0 or r%10==3):
            n-=1
    print(r) 
    t-=1