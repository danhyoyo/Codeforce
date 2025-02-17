l = list(map(int, input().split()))
s = input()
su = 0
for i in s:
    su += l[int(i)-1]
print(su)