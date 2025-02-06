s = input() + "  "
l = len(s)
i = 0
while i<=l-2:
    if(s[i] == '.'):
        i+=1
        print(0,end='')
    elif(s[i:i+2] == "-."):
        i+=2
        print(1, end='')
    elif(s[i:i+2] == "--"): i+=2; print(2, end='')
    else: i+=1