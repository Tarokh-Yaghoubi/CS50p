def main():
    number = get_number()
    tarokh(number)
    

def get_number():
    while True:
        n = int(input("What is n : "))
        if n > 0:
            break
    
    return n

def tarokh(n):
    for _ in range(n):
        print("tarokh")
        
    
main()