def name(x):
     return int(x)*2/10

a=name(10)
print("first sep :",a)


def number(a,b,c,d,e=0):
    print(a+b+c+d+e)
    
number(10 ,50 ,50, 4)

def latter(m,n):
    return m,"cant call me", n

result=latter(str(input("gf name: ")),"vai")
limit=int(input("enter your massge limit :",))
for i in range(1,limit+1,60): # proti bar 60 kora barba
     print(i,"=", result)
     




