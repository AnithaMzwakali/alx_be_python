def main():
    # Create an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrate the __str__ method
    print(my_book)

    # Demonstrate the __repr__ method
    print(repr(my_book))

    # Delete the instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
