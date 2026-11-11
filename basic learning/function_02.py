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



#  *arg *args ব্যবহার করে একটি Function-এ যত ইচ্ছা Positional Arguments পাঠানো যায়।
point = lambda *arg: sum(arg)
print(point(10))



# **kwargs ব্যবহার করে একটি Function-এ যত ইচ্ছা Keyword Arguments পাঠানো যায়।
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Rayhan", age=22, city="Dhaka")


# nested function 

def outer():

    count = 10

    def inner():

        count = 20

        print("Inner:", count)

    inner()

    print("Outer:", count)


outer()


#nested 2 ex;
def main():
    count=0
    def nd():
        nonlocal count
        count +=1
        return count
    return nd
result=main()
print(result())
print(result())
print(result())
print(result())
print(result())
print(result())

def outer():

    def inner():
        return 100

    return inner()


print(outer())



#pass def outer()