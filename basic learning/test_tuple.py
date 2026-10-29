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
temp4.remove(40)
t=tuple(temp4)
print(t)

