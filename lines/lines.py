import sys
import os 

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2: 
    sys.exit("Too few command-line arguments")
elif not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")

elif os.path.exists(sys.argv[1]):
    name = sys.argv[1]
    name, ext = name.split(".")
    
    if ext != 'py': sys.exit("Not a Python file")
    else :

        with open(sys.argv[1], "r") as file:
            i = 0
            lines = file.readlines()
            for line in lines:
                if line.strip() and not line.startswith("#"):
                    i += 1
                else : pass
            print(i)