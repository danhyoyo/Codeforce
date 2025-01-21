n = int(input())
s = input()
anh = 0
du = 0
for i in s:
    if(i == 'A'):
        anh+=1
    else: du+=1
if(anh>du): print("Anton")
elif(anh<du): print("Danik")
else: print("Friendship")