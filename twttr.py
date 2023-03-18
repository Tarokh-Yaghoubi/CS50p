
def main():
    
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    final = []

    name = input("Input: ")

    name = list(name)

    check(name, vowels, final)

    print("Output: ", end="")
    for i in final:
        print(i, end="")


def check(name, vowels, final):
    for i in name:
        if i not in vowels:
            final.append(i)
            
    return final

main()