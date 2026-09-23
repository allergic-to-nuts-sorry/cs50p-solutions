camelcase = input("camelCase: ")
snake = ""

for ch in camelcase:
    if ch.isupper():
        snake+="_"+ch.lower()
    else:
        snake+=ch

print(snake)
