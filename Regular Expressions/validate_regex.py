import re

email = input("What is your email address : ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): print("valid")
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE): print("valid")      # this is a more professional version of the above REGEX 
else : print("Invalid")



def name(name):
    name = input("Enter the name ")
    
    return True if name == "tarokh" else False