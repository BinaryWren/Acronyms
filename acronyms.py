user_input = input("Enter a phrase: ")
acronym = ''.join(word[0].upper() for word in user_input.split())
print(acronym)