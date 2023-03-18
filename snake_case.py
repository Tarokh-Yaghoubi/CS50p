
def main():
    name = input("Enter the file name : ")
    print_snake(name)
    
def print_snake(filename):
    
    camelList = list(filename)

    snake_case = []

    for seek in camelList:
        if seek.isupper():
            seek = "_" + seek.lower()
    
        snake_case.append(seek)

    for i in range(len(snake_case)):
        print(snake_case[i], end="")
        
main()