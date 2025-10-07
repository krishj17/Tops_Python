student={
    "name": "krish",
    "email": "krish@gmail.com",
    "subject": ["java","js","python"]  
}

print(student)
# print(student["name1"])  # gives error if key is not found.
# print(student.get("name1")) # does not gives error if key is not found.

# print(student.keys())
# print(student.values())
# print(student.items())
print(student["subject"][0])
# student["name"]="meet"
student["name1"]="meet"
print(student)