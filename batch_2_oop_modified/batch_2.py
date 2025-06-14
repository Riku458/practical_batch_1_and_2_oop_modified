class Programs:

    # Prog01: Print the smaller number
    def find_smaller(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The smaller number is:", min(num1, num2))

    # Prog02: Print "Not Equal" when the numbers are not the same
    def check_equality(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num1 != num2:
            print("The numbers are Not Equal")
        else:
            print("The numbers are Equal")

    # Prog03: Print the difference of the two numbers
    def find_difference(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The difference is:", (num1 - num2))

    # Prog04: Print the quotient without the decimal point
    def find_quotient_no_decimal(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The quotient is:", int(num1 // num2))

    # Prog05: Print the remainder of division
    def find_remainder(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The remainder is:", num1 % num2)

    # Prog06: First number minus all remaining numbers
    def subtract_remaining(self):
        numbers = [float(input(f"Enter number {num+1}: ")) for num in range(10)]
        result = numbers[0] - sum(numbers[1:])
        print("The result is:", result)

    # Prog07: Count even numbers
    def count_even_numbers(self):
        even_count = 0
        for num in range(10):
            numbers = float(input(f"Enter number {num+1}: "))
            if numbers % 2 == 0:
                even_count += 1
        print("Number of even numbers:", even_count)

    # Prog08: Print odd numbers from 0 to 100 (using while loop)
    def print_odd_numbers(self):
        odd_num = 0
        while odd_num <= 100:
            if odd_num % 2 != 0:
                print(odd_num, end=" ")
            odd_num += 1
        print()

    # Prog09: Print numbers from 0 to 100, excluding those ending in 0 or 5
    def print_special_numbers(self):
        for num in range(101):
            if num % 10 != 0 and num % 10 != 5:
                print(num, end=" ")
        print()

    # Prog10: Print all numbers between two given numbers
    def print_numbers_between(self):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        start = min(num1, num2) + 1
        end = max(num1, num2)
        for numbers in range(start, end):
            print(numbers, end=" ")
        print()