from batch_2 import Programs

if __name__ == "__main__":
    prog = Programs()

    # Run each program
    print("\n--- Prog01: Find Smaller Number ---")
    prog.find_smaller()

    print("\n--- Prog02: Check Equality ---")
    prog.check_equality()

    print("\n--- Prog03: Find Difference ---")
    prog.find_difference()

    print("\n--- Prog04: Find Quotient Without Decimal ---")
    prog.find_quotient_no_decimal()

    print("\n--- Prog05: Find Remainder ---")
    prog.find_remainder()

    print("\n--- Prog06: Subtract Remaining Numbers ---")
    prog.subtract_remaining()

    print("\n--- Prog07: Count Even Numbers ---")
    prog.count_even_numbers()

    print("\n--- Prog08: Print Odd Numbers (0-100) ---")
    prog.print_odd_numbers()

    print("\n--- Prog09: Print Numbers (0-100, Exclude 0/5 Endings) ---")
    prog.print_special_numbers()

    print("\n--- Prog10: Print Numbers Between Two Numbers ---")
    prog.print_numbers_between()