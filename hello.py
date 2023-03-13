
def main():

    name = input("What is your name : ").strip().title()

# Ask user for their name

# Strip() : remove white spaces from string

# split users name into first name and last name 

    first, last = name.split(" ")

    print("Hello", name, sep="???")

    hello(name)

    print(f"Hello {first}")


def hello(to="Someone"):
    print(f"Hello {to}")
    
    
main()