
# 1. Python - Slicing Strings


name = 'rayhan'

print(name[:6])    # শুরু থেকে index 6-এর আগ পর্যন্ত
print(name[0:-5])  # index 0 থেকে শেষের 5 অক্ষর বাদ দিয়ে
print(name[3:5])   # index 3 থেকে 5-এর আগ পর্যন্ত
print(name[0:0])   # empty string '' return করবে
print(name[:-5])  # শুরু থেকে শেষের 5 অক্ষর বাদ দিয়ে
print(name[::5])  # প্রতি 5 ধাপ পর অক্ষর নেবে
print(name[::-3]) # উল্টো দিক থেকে প্রতি 3 ধাপ পর অক্ষর নেবে
print(name[::-1]) # পুরো string উল্টো করবে


# 2. Python - Modify Strings


xyz = 'rayhan hossen'

print(xyz.upper())  # সব অক্ষর বড় হাতের করবে
print(xyz.lower())  # সব অক্ষর ছোট হাতের করবে
print(xyz.strip())  # শুরু ও শেষের extra whitespace সরাবে
print(xyz.replace("hossen", "khan"))  # hossen-এর জায়গায় khan বসাবে
print(xyz.split())  # space অনুযায়ী string-কে list-এ ভাগ করবে
print(xyz.capitalize())  # প্রথম অক্ষর বড়, বাকিগুলো ছোট করবে
print(xyz.title())  # প্রতিটি শব্দের প্রথম অক্ষর বড় করবে


# 3. Python - f-string


nam = 'rayhan'
age = 22

result = nam + " " + str(age)  # integer age-কে string-এ convert করবে
print(result)  # Output: rayhan 22

print(f"my name is {nam} and my age is {age}")
# f-string দিয়ে string-এর মধ্যে variable-এর value বসাবে


# 4. Find Specific Character Index


ra = 'rayhan'

print(ra.index("r"))  # 'r' প্রথম পাওয়া যায় index 0-তে
print(ra.index("a"))  # 'a' প্রথম পাওয়া যায় index 1-এ
print(ra.index("y"))  # 'y' পাওয়া যায় index 2-এ
print(ra.index("n"))  # 'n' পাওয়া যায় index 5-এ

# Note: character না পাওয়া গেলে index() ValueError দেবে
