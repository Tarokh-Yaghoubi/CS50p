def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    puncs = ['.' , ' ' , ',' , '-']
    ans = False
    
    if len(s) > 6 or len(s) < 2:
        ans = False
    
    if len(s) >= 2 and len(s) <= 6:
        for letter in s:
            if letter in puncs:
                ans = False
            else : ans = True

        if s[0:2].isalpha() and s[2:].isalnum():
            ans = True
        else : ans = False                
        
        if '0' in s[0:2] or '0' in s[2] or s[-1].isalpha():
            ans = False
    return ans

main()
