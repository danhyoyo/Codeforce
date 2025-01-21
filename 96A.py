# s= input()
# if(s.find("1111111")!=-1 or s.find("0000000")!=-1): print("YES")
# else: print("NO")
s=input(); print(["NO","YES"]['1'*7 in s or '0'*7 in s])