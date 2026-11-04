#every numm chick even and odd 

x=(input("enter your digit : ").split())
for i in  x:
    if int(i) %2 ==0:
        print(i ,"is even")
    else:
        print(i ,"is odd")