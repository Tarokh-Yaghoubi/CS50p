def main():
    print("WELCOME TO THE GRADES !!!")
    score = int(input("Enter the score : "))
    grade(score)
        

def is_even(n):
    
    return n % 2 == 0


def grade(score):
    
    if is_even(score):
        print("Even")
    else : print("ODD")
    
    if 90 <= score <= 100:
        print("Grade : A")
    elif 80 <= score < 90:
        print("Grade : B")
    elif 70 <= score < 80:
        print("Grade : C")
    elif 60 <= score < 70:
        print("Grade : D")
    else:
        print("Failed !")
        
main()