import math

# Function to compute quadratic roots
def quad_roots(a, b, c):
    y = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + y) / (2 * a)
    x2 = (-b - y) / (2 * a)

    # Return a list containing the two roots
    return [x1, x2]

# Main part of the program
print("Solve for the quadratic equation ax^2 + bx + c = 0")
a = input("Enter the value of a : ")
b = input("Enter the value of b : ")
c = input("Enter the value of c : ")

# Convert the user inputs from string to float
a = float(a)
b = float(b)
c = float(c)

roots = quad_roots(a, b, c)
print("Roots are:", roots[0], roots[1])