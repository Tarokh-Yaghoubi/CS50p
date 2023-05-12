# an Explanation on Object Oriented Programming in Python . 

def main():
    
    student = Student.get()
    print(student)
    



class Student:
    
    def __init__(self, name, city):
        
        self.name = name.title()
        self.city = city

    
    def __str__(self) -> str:
        
        return f"{self.name} lives in {self.city}"
    
    @classmethod
    def get(cls):
        name = input("Type in your name : ")
        city = input("Type in where you live : ")
        return cls(name, city)
    
    # Properties
    
    
    @property
    def name(self):
        return self._name 
    
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")

        self._name = name     
    
    

    @property    
    def city(self):
        return self._city
    
    
    @city.setter
    def city(self, city):
        
        if city not in ["Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid City")
        
        self._city = city
        

if __name__ == "__main__":
    main()
    
