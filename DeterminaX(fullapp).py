import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog

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

# Function to handle the "Calculate Determinant" button click
def calculate_button_click():
    try:
        num_rows = int(simpledialog.askstring("Input", "Enter the number of rows: "))
        num_cols = int(simpledialog.askstring("Input", "Enter the number of columns: "))

        # Get the elements of the matrix from the user
        elements = []
        for i in range(num_rows):
            row_str = simpledialog.askstring("Input", f"Enter row {i + 1} separated by spaces: ")
            row = [float(x) for x in row_str.split()]
            if len(row) != num_cols:
                messagebox.showerror("Error", "Invalid number of elements in the row")
                return
            elements.append(row)

        # Create a NumPy array from the input elements
        matrix = np.array(elements)

        # Calculate and display the determinant
        det = calculate_determinant(matrix)
        messagebox.showinfo("Result", f"Determinant of the matrix is: {det}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except KeyboardInterrupt:
        pass

# Create the main window
root = tk.Tk()
root.title("Matrix Determinant Calculator")

# Create a "Calculate Determinant" button
calculate_button = tk.Button(root, text="Calculate Determinant", command=calculate_button_click)
calculate_button.pack(pady=10)

# Create a "Quit" button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

# Start the GUI main loop
root.mainloop()
