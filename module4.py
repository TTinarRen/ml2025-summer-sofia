# Ask the user for input N (positive integer)
N = int(input("Enter a positive integer N: "))

# Read N numbers one by one
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask the user for input X (integer)
X = int(input("Enter an integer X: "))

# Check if X is in the list of numbers
if X in numbers:
    # Output the index of X
    print(numbers.index(X) + 1)
else:
    # Output -1 if X is not found
    print(-1)