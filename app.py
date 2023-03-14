# A program to check if the user has entered the Great Question of Life , Correctly

def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    x = x.lower().strip()
    if check(x): print("Yes")
    else : print("No")


def check(answer):
    return answer == "42" or answer == "forty-two" or answer == "forty two"


main()