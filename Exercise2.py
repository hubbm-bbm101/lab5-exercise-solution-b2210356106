at_true = 0
dot_true = 0
print("This program's purpose is to check whether you typed an e-mail or not.")
email = str(input("E-mail = "))
number = len(email)
for i in range(0, number):
    if email[i] == "@":
        at_true = 1
    elif email[i] == ".":
        dot_true = 1
    i = i + 1
print(bool(1 == at_true == dot_true))