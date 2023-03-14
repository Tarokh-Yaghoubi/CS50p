# a program to compare two numbers 

def main():
    x = int(input("Enter the first number (x) : "))
    y = int(input("Enter the second number (y) : "))
    compare(x, y)
    

def compare(x, y):
    
    if x > y : print("x is bigger than y")
    elif x < y : print("y is bigger than x")
    else : print("they are equals")
    
    
main()