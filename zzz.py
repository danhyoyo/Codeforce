from collections import defaultdict
st = defaultdict(int)
b = False
st['A'] = 0
st['B'] = 0
st['C'] = 0
for i in range(3):
    s = input()
    if s[1] == '>':
        st[s[2]] += 1
    else:
        st[s[0]] += 1
chuoi = sorted(st.items(), key = lambda x: x[1])
for i in chuoi:
    if i[1] == 0:
        b = True
        break
if b:
    for i in chuoi[::-1]:
        print(i[0],end='')
else:
    print("Impossible")
