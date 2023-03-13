name = input("What is your name : ")

# Using match is a better idea in this program

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "tarokh":
        print("tehran")
    
    case _:
        print("Who ?")
        

# if name == "Harry" or name == "tarokh" or name == "Hermione":
#     print("Gryffindor")
# else:
#     print("Who ?")
    