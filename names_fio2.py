import csv 

students = []

with open("names.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "city": row[1]})
        
        

for student in sorted(students, key= lambda student: student['name']):
    print(f"{student['name']} lives in {student['city']}")