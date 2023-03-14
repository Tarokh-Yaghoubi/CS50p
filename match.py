# Match keyword in Python 
# Same code as we have in ../house.py

def main():
    
    name = input("Enter a name : ")
    name = name.lower()
    does_match(name)

def does_match(username):

    match username:
        
        case "tarokh" | "mohammad" | "sina":
            print("California")
        case "sara":
            print("NYC")
        case _:
            print("Stockholm")
        
main()