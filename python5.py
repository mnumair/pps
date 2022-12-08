#ask user their name
name = input("what's your name? ")

#clear white space at the begining and at the end of the string
name = name.strip()
#change first letter of each word to capital to capitalize the initial letter of the first / middle / last names
name = name.title()


#print out user's name
print(f"hello, {name}")

