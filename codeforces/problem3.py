n=str(input())
then=set(n) #তাহলে set(n) প্রতিটি character আলাদা করে set-এ রাখবে এবং duplicate বাদ দেবে।
if len(then)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")