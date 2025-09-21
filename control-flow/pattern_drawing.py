# pattern_drawing.py

def main():
    # Prompt user for the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    # Start row counter
    row = 0

    # Use a while loop for rows
    while row < size:
        # Use a for loop for columns
        for col in range(size):
            print("*", end="")
        # Move to the next line after each row
        print()
        row += 1


if __name__ == "__main__":
    main()

