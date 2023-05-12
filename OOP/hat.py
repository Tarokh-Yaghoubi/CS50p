import random


class Hat:
    

    house = ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]
    
    
    @classmethod
    def sort(cls, name):
    
        print(name, " is in", random.choice(cls.house))
    
    
Hat.sort("Harry")