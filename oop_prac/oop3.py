class Book():
    def __init__(self, name, author, publisher):
        self.name = name
        self.author = author
        self.publisher = publisher

    def get_book_info(self):
        print(f"""
        Name: {self.name}
        Author: {self.author}
        Publisher: {self.publisher}
""")
        
class BookMetrics(Book):
    def __init__(self, name, author, publisher, release_date, awards, citations):
        super().__init__(name, author, publisher)
        self.release_date = release_date
        self.awards = awards
        self.citations = citations

    def additional_info(self):
        print(f"""
        Release Date: {self.release_date}
        Awards: {self.awards}
        Citations: {self.citations}
""")
        
book_one = BookMetrics("Oliver Twist", "Charles Dickens", "Bentley's Miscellany", "28/06/1948", "Book of the Year", "1,000,000")

book_one.get_book_info()
book_one.additional_info()