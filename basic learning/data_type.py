
# Range and List
number = range(1, 21)
print(list(number))


# Tuple
# Tuple supports indexing, but cannot be changed
random1 = (10, 2, 20, 30, 10, 20, 30, 2, 1, 1, 1, 222, 222)
print(random1)


# List
# List supports indexing and changing items
random10 = [10, 2, 20, 30, 10, 20, 30, 2, 1, 1, 1, 222, 222]
random10[3] = 1000
print(random10)


# Set
# Set does not keep duplicate values
random2 = {10, 2, 20, 30, 10, 20, 30, 2, 1, 1, 1, 222, 222}

# random2[3] = 1000  # Error: set does not support indexing
random2.add(1000)
print(random2)


# Frozen Set
# Frozen set cannot be changed after creation
random3 = frozenset({10, 2, 20, 30, 10, 20, 30, 2, 1, 1, 1, 222, 222})
print(random3)


# Dictionary
# Add, change, and remove values
wub = {
    "name": "rayhan",
    "roll": 4778,
    "id": "0325704778"
}

wub["dep"] = "cse"      # Add a new key-value pair
wub["roll"] = 47780     # Change an existing value
del wub["id"]           # Delete a key-value pair

print(wub)


# Dictionary Loop
for key, value in wub.items():
    print(key, ":", value)


# Boolean
# Boolean has two values: True and False
print(5 < 1)    # False
print(5 < 10)   # True

age = 60
print(age > 59)  # True


# Complex Numbers
# Python uses j for the imaginary part
name = 3 + 7j
age = 7 + 9j

result = (name + age) - (name * age)
print(result)