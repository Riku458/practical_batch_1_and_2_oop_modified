class Programs:

    # Prog01: Get 2 numbers and print the bigger one
    def find_bigger(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num1 == num2:
            print("The numbers are equals")
        else:
            print("The bigger number is:", max(num1, num2))

    # Prog02: Get 2 numbers and check if equal
    def check_equal(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num1 == num2:
            print("The numbers are equal")
        else:
            print("The numbers are not equal")

    # Prog03: Get 2 numbers and return their sum
    def sum_numbers(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sum = num1 + num2
        print("The sum is:", sum)

    # Prog04: Get 2 numbers and return their product
    def product_numbers(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        product = num1 * num2
        print("The produt is:", product)

    # Prog05: Get 2 numbers and return quotient (handles division by zero)
    def quotient_numbers(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            return "Error: Division by zero"
        quotient = num1 / num2
        print("The quotient is:", quotient)

    # Prog06: Get 2 numbers and return num1^num2
    def power_numbers(self):
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent: "))
        exponent_num = num1 ** num2
        print("The result is:", exponent_num)

    # Prog07: Get 10 numbers and return their sum
    def sum_ten_numbers(self):
        total = 0
        for i in range(10):
            num = float(input(f"Enter number {i+1}: "))
            total += num
        print("The total sum is:", total)

    # Prog08: Get 10 numbers and count odd numbers
    def count_odd_numbers(self):
        odd_count = 0
        for i in range(10):
            num = int(input(f"Enter number {i+1}: "))
            if num % 2 != 0:
                odd_count += 1
        print("The total odd number/s is:", odd_count)

    # Prog09: Print even numbers from 0 to 100
    def print_even_numbers(self):
        return [num for num in range(0, 101, 2)]
        
    # Prog10: Print numbers from 0 to 100, excluding those ending with 0
    def print_numbers_except_zero_ending(self):
        return [num for num in range(101) if num % 10 != 0]
