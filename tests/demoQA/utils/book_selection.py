"""
Simple function to randomly select a book from the list of ISBN
"""

import random


class BookSelection:
    def select_a_book():
        book_catalog = [
            '9781449325862', '9781449331818', '9781449337711', '9781449365035',
            '9781491904244', '9781491950296', '9781593275846', '9781593277574'
        ]
    
        book = random.choice(book_catalog)
        return book
      
