from module5_mod import NumberProcessor

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