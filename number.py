# Error Handling in Python , Value Errors or other types of errors (try except)

def main():
    x = get_int("What's X ? ")
    print(f"The X is {x}")


def get_int(prompt):
    
    while True:

        try:

            x = int(input(prompt))
            return x

        except ValueError:
        
            pass
                

main()