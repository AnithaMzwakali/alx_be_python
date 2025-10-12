class Book:
    def __init__(self, title, author, year):
        """
        Constructor: Initializes a Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Returns a readable string representation of the book.
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an unambiguous representation that can recreate the object.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: Called when the object is about to be deleted.
        Prints a message indicating the book is being deleted.
        """
        print(f"Deleting {self.title}")
