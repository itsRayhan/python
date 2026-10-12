number= range(1,21) #range data type
print(list(number)) #list keyword

#index not support (){} support only[]
random1=(10,2,20,30,10,20,30,2,1,1,1,222,222)
print(random1)
random10=[10,2,20,30,10,20,30,2,1,1,1,222,222]
random10[3]=1000
print(random10)
#when use {} its gonna working a set behavoir 
#set একই value একাধিকবার রাখে না।
random2={10,2,20,30,10,20,30,2,1,1,1,222,222} 
#random2[3]=1000 #error
random2.add(1000) #correct
print(random2) #output:{1, 2, 20, 10, 222, 30}


random3=frozenset({10,2,20,30,10,20,30,2,1,1,1,222,222} )
print(random3)




#dictionary valu add,change,remove
wub={
    "name":"rayhan",
    "roll":4778,
    "id":"0325704778"
}
wub["dep"]="cse"   #add
wub["roll"]=47780  #change
del wub["id"]      #delete
print(wub)
#dictionary new line 
for key, value in wub.items():
    print(key, ":", value)




#bool ahve two keyword true and false they chick is correct or incorect
print(5<1)#False
print(5<10) #True

age=60
print(age>59) #True



#complex syentex use only i and j
name= 3+7j
age =7+9j
result=(name+age)-(name*age)
print(result)