def main():
    print_square(10)
    
    
def print_brick(size):
    print("#" * size, end="")
    
def print_square(size):
    
    for i in range(size):
        
        print_brick(size);

        print()
main()