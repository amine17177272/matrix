import numpy as np

# Create the input message
input_message = """
What do you want to do?
c => Calculate the determinant of a matrix
q => Quit
Choose one option: """

# Command list
command_list = ["c", "q"]

# Define the calculate_determinant function
def calculate_determinant(matrix):
    # Check if the matrix is square
    num_rows, num_cols = matrix.shape
    if num_rows != num_cols:
        raise ValueError("Matrix is not square")

    # Base case: If the matrix is 1x1, return the only element as the determinant
    if num_rows == 1:
        return matrix[0, 0]

    # Base case: If the matrix is 2x2, return the determinant using the formula
    if num_rows == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    determinant = 0
    for col in range(num_cols):
        submatrix = np.delete(matrix, 0, axis=0)
        submatrix = np.delete(submatrix, col, axis=1)
        determinant += matrix[0, col] * calculate_determinant(submatrix) * (-1) ** col

    return determinant

# Main loop
while True:
    user_input = input(input_message).lower().strip()

    if user_input == "q":
        print("Exiting the program.")
        break
    elif user_input == "c":
        try:
            num_rows = int(input("Enter the number of rows: "))
            num_cols = int(input("Enter the number of columns: "))

            # Get the elements of the matrix from the user
            print("Enter the elements of the matrix row by row:")
            elements = []
            for i in range(num_rows):
                row = [float(x) for x in input(f"Enter row {i + 1} separated by spaces: ").split()]
                if len(row) != num_cols:
                    raise ValueError("Invalid number of elements in the row")
                elements.append(row)

            # Create a NumPy array from the input elements
            matrix = np.array(elements)

            # Calculate and print the determinant
            det = calculate_determinant(matrix)
            print("Determinant of the matrix is:", det)

        except ValueError as e:
            print("Error:", e)
        except KeyboardInterrupt:
            print("\nMatrix input aborted.")
    else:
        print(f"Sorry, command '{user_input}' is not found.")

    # Ask if the user wants to perform another operation
    another_operation = input("Do you want to perform another operation? (yes/no): ").lower().strip()
    if another_operation != 'yes':
        print("Goodbye!")
        break







