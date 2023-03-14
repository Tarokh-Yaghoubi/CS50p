def main():
    expression = input("Enter the expression : ").lower().strip()
    interpreter(expression)
    
def interpreter(expression):
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    
    match y:
        case '+':
            answer = float(x) + float(z)

        case '-':
            answer = float(x) - float(z)
            
        case '*':
            answer = float(x) * float(z)
            
        case '/':
            answer = float(x) / float(z)
            
        case _:
            answer = 0.0
            print("Wrong Operator Detected")
            
    
    print(answer)
                
main()