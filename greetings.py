# Check if the reply is hello , or starts with an h , or none 

def main():
    message = input("Greetings : ")
    message = message.lower().strip()
    check(message)
    
def check(reply):
    if reply == "hello":
        print("$0")
    elif reply[0] == "h" and reply != "hello":
        print("$20")
    else : print("$100")
    
main()