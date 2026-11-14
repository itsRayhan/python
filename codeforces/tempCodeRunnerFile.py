n= input()
count =0
for i in  n:
    if i=="4" or i=="7":
        count+=1
    l= len(i)
    if l==4 or l==7:
        print("YES")
    else:
        print("NO")