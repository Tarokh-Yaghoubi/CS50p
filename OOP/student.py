# EXPLANATION OF OOP - OBJECT ORIENTED PROGRAMMING

class Student:
    
    def __init__(self, first, last, house, middle=None):
        if not first:
            raise ValueError("Missing First Name")

        if house not in ["London", "Tehran", "Berlin", "Ravenclaw"]:
            raise ValueError("Wrong House")
        
        self.first = first
        self.middle = middle
        self.last = last
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_house()
        
   # print(f"{student.name} from {student.city}")
    print(student)

# def get_name():
#    return input("Type in your name: ")
    

# def get_house():
#    return input("Type in your city: ")


def get_house():
    
    first = input("First Name : ")
    middle = input("Middle Name : ")
    last = input("Last Name : ")
    house = input("House : ")
    return Student(first, last, house, middle) 


if __name__ == "__main__":
    main()