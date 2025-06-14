from batch_1 import Programs

# Run each program
if __name__ == "__main__":
    program = Programs()

    print("\n--- Prog01: Bigger Number ---")
    program.find_bigger()

    print("\n--- Prog02: Check Equal ---")
    program.check_equal()

    print("\n--- Prog03: Sum of Two Numbers ---")
    program.sum_numbers()

    print("\n--- Prog04: Product of Two Numbers ---")
    program.product_numbers()

    print("\n--- Prog05: Quotient of Two Numbers ---")
    program.quotient_numbers()

    print("\n--- Prog06: Power of Two Numbers ---")
    program.power_numbers()

    print("\n--- Prog07: Sum of 10 Numbers ---")
    program.sum_ten_numbers()

    print("\n--- Prog08: Count Odd Numbers ---")
    program.count_odd_numbers()

    print("\n--- Prog09: Even Numbers (0-100) ---")
    print(program.print_even_numbers())

    print("\n--- Prog10: Numbers (0-100) Excluding Zero-Ending ---")
    print(program.print_numbers_except_zero_ending())