class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        """Reads N numbers from the user."""
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def find_number(self, x):
        """Finds the index of X in the list of numbers."""
        if x in self.numbers:
            return self.numbers.index(x) + 1  # Return 1-based index
        else:
            return -1  # Return -1 if not found


def main():
    # Ask the user for input N (positive integer)
    N = int(input("Enter a positive integer N: "))

    # Create an instance of NumberProcessor
    processor = NumberProcessor()

    # Read N numbers
    processor.read_numbers(N)

    # Ask the user for input X (integer)
    X = int(input("Enter an integer X: "))

    # Find and output the result
    result = processor.find_number(X)
    print(result)


if __name__ == "__main__":
    main()