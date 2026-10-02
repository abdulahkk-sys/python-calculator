import time

def calculator():
    print("===== Python Calculator =====")

    while True:
        print("\nOperations: +  -  *  /")
        print("Enter 'q' to quit")

        operator = input("Enter operation: ")

        if operator.lower() == 'q':
            print("Calculator closed.")
            break

        if operator not in ['+', '-', '*', '/']:
            print("Invalid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            start_time = time.perf_counter()

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2

            end_time = time.perf_counter()

            execution_time = end_time - start_time

            print(f"Result: {result}")
            print(f"Execution Time: {execution_time:.10f} seconds")

        except ValueError:
            print("Please enter valid numbers.")


calculator()