students = []
with open("names.csv") as file:    
    for line in (file):
        
        name, city = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["city"] = city
        students.append(student)
    
    
for student in students:
    print(f"{student['name']} is in {student['city']}")    
    