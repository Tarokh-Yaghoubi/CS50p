# A program to get a score and return a grade 

def main():
    x = int(input("Enter the score : "))
    grade(x)
    

def grade(score):
    
    if 90 <= score <= 100:
        print("Grade : A")
    elif 80 <= score < 90:
        print("Grade : B")
    elif 70 <= score < 80:
        print("Grade : C")
    elif 60 <= score < 70:
        print("Grade : D")
    else : print("Failed")


main()