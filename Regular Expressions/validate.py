
'''
    This code is an Introduction to Programming in Python (Regex)
    This program shows that it is very hard to find out if an email address is valid using python itself 
    This program shows the importance of regular expressions

'''


email = input("What is your email : ").strip()

# tarokhgit@gmail.com

username, domain = email.split("@")

if username and domain.endswith(".com"): 
    print("valid")
    
else : print("invalid")