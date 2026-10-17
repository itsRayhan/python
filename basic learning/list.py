x = ["apple", "banana", "cherry"]
print(len(x)) #here len  is length 
print(type(x))  # what is the data type

x2=['apple2']
x[2]='banana' #change item
# x[4]='lissi'  invallid

x.append('lissi')            #.append() — শেষে item যোগ করা
x.insert(6,'fruit')          #insert() — নির্দিষ্ট position-এ যোগ করা
x.extend(x2)                 #extend() — অন্য list-এর items যোগ করা
x.remove('apple') 
x.pop(1)                     #pop() — index দিয়ে delete
del x2[0]                    #del fruits[0]	নির্দিষ্ট index delete করে
del x2	                     #Variable delete করে
x.clear()


print (x) #access list item
q = ["apple", "banana", "cherry","marry"]
#loop list
for i in q:   #this loop worked in item , means call item 
    print(i)

#use index and call item
print('use index:') 
for i in range (len(q)):
     
    print(q[i])



#use while loop 
i=0
while i<(len(q)):
    if i==3:
        break
    i+=1
    print(q[i])



