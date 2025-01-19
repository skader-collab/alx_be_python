# library_management.py

class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """
        Initialize the book with a title, author, and its availability status.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark the book as checked out if it is available.
        Return True if the operation is successful, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Mark the book as available if it is currently checked out.
        Return True if the operation is successful, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Check if the book is available.
        Return True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        """
        Initialize the library with an empty collection of books.
        """
        self._books = []

    def add_book(self, title, author):
        """
        Add a new book to the library collection.
        """
        new_book = Book(title, author)
        self._books.append(new_book)
        print(f"Book added: '{title}' by {author}")

    def check_out_book(self, title):
        """
        Check out a book by its title.
        If the book is available, mark it as checked out and return True.
        If the book is not found or is already checked out, return False.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book not found: '{title}'")
        return False

    def return_book(self, title):
        """
        Return a book to the library by its title.
        If the book is currently checked out, mark it as available and return True.
        If the book is not found or is already available, return False.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book not found: '{title}'")
        return False

    def list_available_books(self):
        """
        List all books in the library that are currently available.
        Return a list of strings with the title and author of each available book.
        """
        available_books = [
            f"{book.title} by {book.author}"
            for book in self._books if book.is_available()
        ]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available.")
        return available_books


# Example Usage
if __name__ == "__main__":
    library = Library()

    # Add books to the library
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    # List available books
    library.list_available_books()

    # Check out a book
    library.check_out_book("1984")

    # List available books after checking out a book
    library.list_available_books()

    # Return the book
    library.return_book("1984")

    # List available books after returning the book
    library.list_available_books()
