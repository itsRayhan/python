
# PYTHON TUPLE - ALL OPERATIONS



t1 = (10, 20, 30, 40)
t2 = ("apple", "banana", "mango")
t3 = (10, "Rayhan", 3.29, True)
t4 = ()
t5 = (10,)
t6 = 10, 20, 30

print(t1)
print(t2)
print(t3)
print(type(t4))
print(type(t5))
print(type(t6))


# 2. Access Tuple
print("\n--- 2. Access Tuple ---")

t = ("apple", "banana", "mango", "orange")

print(t[0])
print(t[1])
print(t[-1])
print(t[-2])
print(t[1:3])
print(t[:2])
print(t[2:])
print(t[::2])
print(t[::-1])


# 3. Update Tuple
print("\n--- 3. Update Tuple ---")

t = (10, 20, 30, 40)

temp = list(t)
temp[1] = 99
t = tuple(temp)

print(t)


# 4. Add Items
print("\n--- 4. Add Items ---")

t = (10, 20, 30)

t = t + (40,)
print(t)

t = t + (50, 60)
print(t)


# 5. Remove Items
print("\n--- 5. Remove Items ---")

t = (10, 20, 30, 40)

temp = list(t)
temp.remove(20)
t = tuple(temp)

print(t)


# 6. Unpack Tuple
print("\n--- 6. Unpack Tuple ---")

student = ("Rayhan", 22, "CSE")

name, age, department = student

print(name)
print(age)
print(department)


# 7. Unpacking with *
print("\n--- 7. Unpacking with * ---")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# 8. Loop Through Tuple
print("\n--- 8. Loop Through Tuple ---")

t = ("apple", "banana", "mango")

for item in t:
    print(item)

i = 0
while i < len(t):
    print(t[i])
    i += 1

for i, item in enumerate(t):
    print(i, item)


# 9. Join Tuples
print("\n--- 9. Join Tuples ---")

t1 = (10, 20, 30)
t2 = (40, 50, 60)

print(t1 + t2)
print(t1 * 3)

my_list = [1, 2, 3]
print(tuple(my_list))


# 10. Tuple count()
print("\n--- 10. count() ---")

t = (10, 20, 10, 30, 10, 40)

print(t.count(10))


# 11. Tuple index()
print("\n--- 11. index() ---")

t = (10, 20, 30, 20, 40)

print(t.index(20))
print(t.index(20, 2))


# 12. Length, Min, Max, Sum
print("\n--- 12. Built-in Functions ---")

t = (10, 20, 30, 40)

print(len(t))
print(min(t))
print(max(t))
print(sum(t))


# 13. Membership Operators
print("\n--- 13. Membership ---")

t = (10, 20, 30, 40)

print(20 in t)
print(50 not in t)


# 14. Sort Tuple
print("\n--- 14. Sort Tuple ---")

t = (40, 10, 30, 20)

print(tuple(sorted(t)))
print(tuple(sorted(t, reverse=True)))


# 15. Reverse Tuple
print("\n--- 15. Reverse Tuple ---")

t = (10, 20, 30, 40)

print(tuple(reversed(t)))


# 16. Copy Tuple
print("\n--- 16. Copy Tuple ---")

t1 = (10, 20, 30)
t2 = tuple(t1)

print(t2)
print(t1 == t2)


# 17. Check Item Exists
print("\n--- 17. Check Item ---")

fruits = ("apple", "banana", "mango")

if "banana" in fruits:
    print("Found")
else:
    print("Not found")


# 18. Delete Tuple
print("\n--- 18. Delete Tuple ---")

t = (10, 20, 30)

del t

print("Tuple variable deleted")


# 19. Tuple Comparison
print("\n--- 19. Tuple Comparison ---")

t1 = (10, 20, 30)
t2 = (10, 20, 30)
t3 = (10, 20, 40)

print(t1 == t2)
print(t1 != t3)
print(t1 < t3)


# 20. Nested Tuple
print("\n--- 20. Nested Tuple ---")

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


# 21. any() and all()
print("\n--- 21. any() and all() ---")

t1 = (True, True, True)
t2 = (True, False, True)
t3 = (0, 1, 2)

print(all(t1))
print(all(t2))
print(any(t2))
print(any((0, 0, 0)))
print(all(t3))


# 22. Tuple Comprehension
print("\n--- 22. Generator to Tuple ---")

t = tuple(x for x in range(1, 6))

print(t)


# 23. Tuple Length and Type
print("\n--- 23. Length and Type ---")

t = (10, 20, 30)

print(len(t))
print(type(t))


# 24. Concatenation and Repetition
print("\n--- 24. Operators ---")

t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)
print(t1 * 3)


# 25. Nested Tuple Access
print("\n--- 25. Nested Tuple Access ---")

data = ((1, 2), (3, 4), (5, 6))

print(data[0][0])
print(data[1][1])
print(data[2][0])


# ==========================================
# END OF PYTHON TUPLE PRACTICE
# ==========================================

print("\nAll Tuple Operations Completed!")

