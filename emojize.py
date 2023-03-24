import emoji

inp = input("Input : ")
print("Output: ", end="")
print(emoji.emojize(inp, language='alias'))