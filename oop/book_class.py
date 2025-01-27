class Book:
    def __init__(self, title, author, year):
       
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
       
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """
        String representation of the Book instance.
        :return: A user-friendly string describing the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the Book instance.
        :return: A string that recreates the Book instance.
        """
        return f"Book({self.title}, '{self.author}', {self.year})"

# Example Usage:
if __name__ == "__main__":
    # Creating a book instance
    my_book = Book(1984, "George Orwell", 1949)
    
    # Printing string representation
    print(str(my_book))  # Output: '1984' by George Orwell, published in 1949

    # Printing official representation
    print(repr(my_book))  # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the book instance
    del my_book
