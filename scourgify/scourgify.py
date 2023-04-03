import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        inp = sys.argv[1]
        out = sys.argv[2]
        inp, ext1 = inp.split(".")
        out, ext2 = out.split(".")
        if ext1 != "csv" or ext2 != "csv":
            sys.exit("Not a CSV file")
        else:
            mv(sys.argv[1], sys.argv[2])
 


def mv(file, file2):
    try:
        
        with open(file, "r") as f:
            lines = csv.DictReader(f)
   
            with open(file2, "w") as f:
                header = ["first", "last", "house"]                
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                for student in lines:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
                
    except FileNotFoundError:
        sys.exit("File Not Found")
"""
for student in students:
    print(student['firstname'], student['lastname'], student['house'])"""
    

if __name__ == "__main__":
    main()