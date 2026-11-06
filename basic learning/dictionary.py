cdic = {
    "name": "rayhan",
    "roll": 4778,
}
print(cdic)
print(cdic["name"]) #access dictionalry 
print(cdic.get("email")) #get means value na thka o error asba na
cdic["email"]= "mdrayhan.dev@gmail.com" #value add
print(cdic)
cdic.setdefault("age", 22)
cdic["roll"]= 30254778
print(cdic)
cdic.update({"roll": 548576812849681684685616 })
print(cdic)
cdic_new= cdic.copy()
print(cdic)
cdic.pop("name")
cdic.popitem()
del cdic["roll"]
del cdic
#cdic.clear()


print(cdic_new)

student = {
    "name": "Rayhan",
    "age": 22,
    "department": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())


for x in student:
    print(x)
for x in student.values():
    print(x)
for key, value in student.items():
    print(key, "=", value)