t = int(input())
while t:
    n = int(input())
    ans = n//3
    if n % 3 == 0:
        print(ans,ans)
    elif n % 3 == 1:
        print(ans+1,ans)
    else:
        print(ans,ans+1)
    t -=1