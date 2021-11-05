print("This program's purpose is to calculate the sum of odd numbers and average of the even numbers UP TO the \n "
      "positive number typed. (The number you typed is included.)")
number = int(input("Your Number = "))
result_1 = 0
result_2 = 0
if number < 0:
    print("The number you typed is negative.")
else:
    for i in range(1, number + 1, 2):
        if number == 0:
            print("The sum of the odd numbers up to the one you typed is 0")
            break
        else:
            result_1 = result_1 + i
    print("The sum of the odd numbers up to the one you typed is", result_1)
    for i in range(0, number + 1, 2):
        result_2 = result_2 + i
    quantity = number / 2
    if quantity == 0:
        quantity = quantity + 1
    result_2 = result_2 / int(quantity)
    print("The average of the even numbers up to the one you typed is", result_2)