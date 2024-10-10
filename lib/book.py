#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, author: str, genre: str, page_count: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.page_count = page_count  # This will call the setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
