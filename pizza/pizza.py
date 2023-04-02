import sys 
import csv 
from tabulate import tabulate

def main():
    if len(sys.argv) > 2 : sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2 : sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        name = sys.argv[1]
        name, ext = name.split(".")
        if ext != 'csv' : sys.exit("Not a csv file")
        else : print(pizza(sys.argv[1]))
        

def pizza(file):
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            return table
    
    except FileNotFoundError:
        sys.exit("File did not found")
        
        

if __name__ == "__main__":
    main()