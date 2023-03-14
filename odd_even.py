# Check if the number is odd or even 

def main():
    
    x = int(input("Enter a number : "))
    if is_even(x): print("it's Even")
    else: print("Odd")
    

def is_even(number):
    
    # This type of programming is called Pythonic (we only see these things in Python)
    # return True if number % 2 == 0 else False 
    return number % 2 == 0

main()