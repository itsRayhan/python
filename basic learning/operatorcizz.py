x=3
y=5
z=3

print(x+y)
print(x-y)
print(x*y)
print("division",x/y)

print(y**x) #to the power
print(x%y)  #(ভাগশেষ)
print(x//y)  #astra sonkha like 3.3457 not show 3 only

#!=	Not equal	
if x != y:
    print("true")
else:
    print("flase")


#Logical Operators
if x<4 and y>6:
    print ("1st ok")
elif x>4 or y>6:
    print ("2nd ok")
elif not (x>4 and y<6):
    print("3rd is ok")
else:
    print("somthing is happend")


#Python Identity Operators is and is not
print (x is z)
print (x is not y)


#Membership Operators
h='rayhan'
print('r' in h)
print ('d' not in h)

