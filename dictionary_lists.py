students = [
    
    {
        "name":"Harry",
        "house": "Gryffindor",
        "major": "magician"
    },
    {
        "name": "Tarokh",
        "house": "Koln",
        "major": "programmer"
    },
    {
        "name": "Merlin",
        "house": "Camelot",
        "major": "wizard"
    },
    {
        "name": "voldemort",
        "house": "Gryffindor",
        "major": None
    }
]


for student in students:
    print(student["name"], student["house"], student["major"], sep=" ->  ")
