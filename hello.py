# Ask user for their name 
name = input("What is your name : ").strip().title()

# Strip() : remove white spaces from string

# split users name into first name and last name 

first, last = name.split(" ")


print("Hello", name, sep="???")

print(f"Hello {name}")

print('Hello "friend" ')

print(f"Hello {first}")

print("the dude writing these programs is called \"tarokh\" ")