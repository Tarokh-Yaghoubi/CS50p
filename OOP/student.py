# An explanation on object-oriented programming 


class Student:
    
    def __init__(self, first, last, country, city=None):
        
        ''' This syntax is Pythonic '''
        
        if not first:
            raise ValueError("You did'nt enter a name ... ")

        if city not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Wrong City ... ")
                
        self.first = first
        self.last = last
        self.country = country
        self.city = city
        
     #   print(f"{self.name} lives in {self.city}")
        ''' this is also a comment '''
    
    def __str__(self):
        return f"{self.first} from {self.country}"

def main():
#    users = ["tarokh", "harry", "karim", "jacob", "jorge"]
    
    student = get_person()
#    if student.name not in users:
#        student.city = "Ravenclaw"

    print(student)
    
def get_person():
    
    first = input("Type in your name ... ")
    last = input("Type in your last name ... ")
    country = input("Type in your country ... ")
    city = input("Which city do you live in ... ")
    return Student(first, last, country, city) 

if __name__ == "__main__":
    main()