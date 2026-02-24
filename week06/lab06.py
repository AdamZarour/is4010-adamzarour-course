# lab06.py

class Book:
    """
    A simple representation of a physical book.

    Parameters
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The publication year of the book.
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author} ({self.year})"

    def get_age(self) -> int:
        """
        Calculate the age of the book assuming the current year is 2025.

        Returns
        -------
        int
            The age of the book in years.
        """
        current_year = 2025
        return current_year - self.year


class EBook(Book):
    """
    A digital book that extends Book by adding file size.

    Parameters
    ----------
    title : str
        The title of the ebook.
    author : str
        The author of the ebook.
    year : int
        The publication year of the ebook.
    file_size : int
        File size in megabytes.
    """

    def __init__(self, title: str, author: str, year: int, file_size: int):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} ({self.file_size} MB)"


if __name__ == "__main__":
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(book)
    print("Age:", book.get_age())

    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook)
    print("Age:", ebook.get_age())