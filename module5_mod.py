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