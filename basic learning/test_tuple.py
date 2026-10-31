t1 =(10,"rayhan",3.56)
t2=(19,38)
print(t1)
print(type(t2))

print(t1[2])
print(t1[-3])  #- reverse 
print(t1[::3]) # 2 index pass at a time 

#update
print (list(t1))
temp = list(t2)
temp[1]=30
t2= tuple(temp)
print("update output: ", t2)


#add
t2=t2+(60,)
print("add",t2)


#index a add 

t2=(5,)+ t2 +(3,)
print("index :", t2)

#middle and last add tin taple
t=(10,20,30,40,50)
t=t[:3]+(5,)+t[3:]
print("out 5 :  ",t)
t=t[:7]+(15,)+t[7:]
print("ou15t  :  ",t)

#remoe through slice 
temp2=t[:2]+t[3:]
print(temp2)

#remove pop and remove 

temp3= list(t)
temp3.remove(50)
t=tuple(temp3)
print(t)

temp4= list(t)
temp4.pop(4)  # pop korla index dea pop korat hoi like remove 
t=tuple(temp4)
print("pop",t)

# 25. Nested Tuple Access
data = ((1, 2), (3, 4), (5, 6))

print(data[0][0])
print(data[1][1])
print(data[2][0])

#unpack tuple
wub =("rayhan", 4778, "cse")
*name, roll , dep, =wub
print(name)
print (roll)
print (dep)

num=(90,50,60,40,30,50)
start , *mid ,end =num
print(start)
print (mid)
print (end)

# 8. Loop Through Tuple
print("\n--- 8. Loop Through Tuple ---")

t = ("apple", "banana", "mango")

for i, item in enumerate(t):
    print(i, item)

print(list(enumerate(t)))        #enumerate mana index no



t1 = (10, 20, 30)
t2 = (40, 50, 60)

print(t1 + t2)
print(t1 * 3)

print(wub.count(4778))

t8 = (10, 20, 30, 20, 40)

print(t8.index(20))
print(t8.index(20, 0 ,3))


t = (10, 20, 30, 40)
a=10
b=30
print(len(t))
print(min(t))
print(max(t))
print(sum(t))


t = (10, 20, 30, 40)

print(20 in t)
print(50 not in t)


t = (40, 10, 30, 20)
print(tuple(sorted(t)))
print(tuple(sorted(t, reverse= False)))









# important sorted easy way
number = [10, 20, 3, 3, 500, 9]
print(sorted(number))

#comarison 
t1 = (10, 20, 50)
t2 = (10, 20, 30)
t3 = (10, 20, 40)

print(t1 == t2)
print(t1 != t3)
print(t1 < t3)










t = (
    ("Rayhan", 22),
    ("Sajon", 23),
    ("Mithu", 21)
)

print(t[0])
print(t[0][0])
print(t[1][1])


for student in t:
    print(student)


    
t1 = (True, True, True)
t2 = (True, False, True)
t3 = (0, 1, 2)

print(all(t1))
print(all(t2))
print(any(t2))
print(any((0, 0, 0)))
print(any(t3))


t = tuple(x for x in range(1, 6))

print(t) #(1, 2, 3, 4, 5)

print("END")