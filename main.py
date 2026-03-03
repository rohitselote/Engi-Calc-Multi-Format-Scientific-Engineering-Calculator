import numpy as np


def get_matrix(name: str) -> np.ndarray:

    print(f"\nEnter elements of {name} (row by row).")
    print("Use space between numbers. Press Enter on empty line to finish.\n")
    rows = []
    while True:
        row_input = input("Row (empty to stop): ").strip()
        if row_input == "":
            break
        try:
            row = [float(x) for x in row_input.split()]
            if rows and len(row) != len(rows[0]):
                print("All rows must have the same number of columns. Try again.")
                continue
            rows.append(row)
        except ValueError:
            print("Invalid row. Please enter numbers only.")
    if not rows:
        print("No data entered. Using empty matrix.")
        return np.array([[]])
    return np.array(rows, dtype=float)


def matrix_menu():
    while True:
        print("\n=== Matrix Algebra (NumPy) ===")
        print("1. Matrix Addition (A + B)")
        print("2. Matrix Subtraction (A - B)")
        print("3. Matrix Multiplication (A × B)")
        print("4. Determinant of a Matrix")
        print("5. Inverse of a Matrix")
        print("6. Transpose of a Matrix")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice in {"1", "2", "3"}:
            A = get_matrix("A")
            B = get_matrix("B")
            try:
                if choice == "1":
                    result = A + B
                    print("\nResult (A + B):")
                elif choice == "2":
                    result = A - B
                    print("\nResult (A - B):")
                else:  # "3"
                    result = A @ B
                    print("\nResult (A × B):")
                print(result)
            except ValueError as e:
                print(f"Operation not possible: {e}")
        elif choice == "4":
            A = get_matrix("A")
            try:
                det = float(np.linalg.det(A))
                print(f"\nDeterminant: {det}")
            except np.linalg.LinAlgError as e:
                print(f"Error computing determinant: {e}")
            except ValueError as e:
                print(f"Invalid matrix for determinant: {e}")
        elif choice == "5":
            A = get_matrix("A")
            try:
                inv = np.linalg.inv(A)
                print("\nInverse of matrix:")
                print(inv)
            except np.linalg.LinAlgError as e:
         
                print(f"Matrix is singular or not invertible: {e}")
            except ValueError as e:
                print(f"Invalid matrix for inversion: {e}")
        elif choice == "6":
            A = get_matrix("A")
            print("\nTranspose of matrix:")
            print(A.T)
        else:
            print("Invalid choice. Please try again.")


def get_numbers() -> list[float]:
    """
    Prompt user for a list of numbers separated by spaces.
    """
    while True:
        raw = input("\nEnter numbers separated by spaces: ").strip()
        try:
            numbers = [float(x) for x in raw.split()]
            if not numbers:
                print("You must enter at least one number.")
                continue
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def statistics_menu():
    while True:
        print("\n=== Statistical Analysis ===")
        print("1. Mean")
        print("2. Median")
        print("3. Standard Deviation")
        print("4. All (Mean, Median, Std Dev)")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            break

        data = np.array(get_numbers(), dtype=float)

        if choice == "1":
            print(f"\nMean: {np.mean(data)}")
        elif choice == "2":
            print(f"\nMedian: {np.median(data)}")
        elif choice == "3":
            print(f"\nStandard Deviation: {np.std(data, ddof=1)}")
        elif choice == "4":
            print(f"\nMean: {np.mean(data)}")
            print(f"Median: {np.median(data)}")
            print(f"Standard Deviation: {np.std(data, ddof=1)}")
        else:
            print("Invalid choice. Please try again.")


def unit_conversion_menu():
    while True:
        print("\n=== Unit Conversions ===")
        print("1. Length")
        print("2. Weight/Mass")
        print("3. Temperature")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        else:
            print("Invalid choice. Please try again.")


def safe_float_input(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please try again.")


def length_conversion():
    print("\n--- Length Conversions ---")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Meters to Centimeters")
    print("4. Centimeters to Meters")
    print("5. Meters to Feet")
    print("6. Feet to Meters")

    choice = input("Choose an option: ").strip()

    value = safe_float_input("Enter value: ")

    try:
        if choice == "1":
            result = value / 1000.0
            print(f"{value} m = {result} km")
        elif choice == "2":
            result = value * 1000.0
            print(f"{value} km = {result} m")
        elif choice == "3":
            result = value * 100.0
            print(f"{value} m = {result} cm")
        elif choice == "4":
            result = value / 100.0
            print(f"{value} cm = {result} m")
        elif choice == "5":
            result = value * 3.28084
            print(f"{value} m = {result} ft")
        elif choice == "6":
            result = value / 3.28084
            print(f"{value} ft = {result} m")
        else:
            print("Invalid choice.")
    except ZeroDivisionError:
        print("Division by zero error during conversion.")


def weight_conversion():
    print("\n--- Weight/Mass Conversions ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    choice = input("Choose an option: ").strip()

    value = safe_float_input("Enter value: ")

    try:
        if choice == "1":
            result = value * 2.20462
            print(f"{value} kg = {result} lb")
        elif choice == "2":
            result = value / 2.20462
            print(f"{value} lb = {result} kg")
        else:
            print("Invalid choice.")
    except ZeroDivisionError:
        print("Division by zero error during conversion.")


def temperature_conversion():
    print("\n--- Temperature Conversions ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option: ").strip()
    value = safe_float_input("Enter temperature: ")

    try:
        if choice == "1":
            result = (value * 9.0 / 5.0) + 32.0
            print(f"{value} °C = {result} °F")
        elif choice == "2":
            result = (value - 32.0) * 5.0 / 9.0
            print(f"{value} °F = {result} °C")
        else:
            print("Invalid choice.")
    except ZeroDivisionError:

        print("Division by zero error during conversion.")


def main():
    while True:
        print("\n==============================")
        print("  Engi-Calc: Multi-Format Scientific & Engineering Calculator")
        print("==============================")
        print("1. Matrix Algebra (NumPy)")
        print("2. Statistical Analysis")
        print("3. Unit Conversions")
        print("0. Exit")

        choice = input("Select a module: ").strip()

        if choice == "0":
            print("Exiting Engi-Calc. Goodbye!")
            break
        elif choice == "1":
            matrix_menu()
        elif choice == "2":
            statistics_menu()
        elif choice == "3":
            unit_conversion_menu()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")

