def numbers(*args):#Function তৈরি করেছো ২টি Parameter দিয়ে। কিন্তু কখনো ৩টি, কখনো ৫টি, আবার কখনো ১০টি Argument পাঠাতে চাও।
    #print(args)
    total=0
    for i in args:
        total +=i
    return total 
print(numbers(10, 20, 30, 40, 50))


#global bariable 
age = 22
def student():
    global age
    age = 25
student()
print(age)





check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(10))
print(check(7))



