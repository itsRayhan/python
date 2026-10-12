x,y,z='rayhan','janina','nextojanina'
print("run serial :",x,y,"\n",z)
#print(y)
#print(z)
a=b="me"
print(a)
print(b)
ty='ray'
#i='han'
i=7
print(ty+str(i))
name='rayhan'
def change():
    global name #only inside the function need global
    name = "Python"
    print(name)

change()
print(name)















name = "Rayhan"

def change():
    global name
    name = "Python"

change()
print(name)

name = "Java"
print(name)