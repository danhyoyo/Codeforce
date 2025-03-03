n, k = map(int, input().split())
st = ''
while n:
    s = input()
    st += s
    n-=1
if 'C' in st or 'M' in st or 'Y' in st:
    print("#Color")
else:
    print("#Black&White")