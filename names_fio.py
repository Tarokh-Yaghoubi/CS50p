students = []

with open("names.csv", "r") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name": name, "city": city}
        students.append(student)
    
def get_name(student):
    return student['name']

for student in sorted(students, key= lambda student: student['city'], reverse=True):
    print(f"{student['name']} lives in {student['city']}")