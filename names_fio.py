students = []

with open("names.csv", "r") as file:

    for line in file:
        student = {}
        name, city = line.rstrip().split(",")
        student["name"] = name
        student["city"] = city
        students.append(student)
        

for student in students:
    print(f"{student['name']} is living in {student['city']}")