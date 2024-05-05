from json import dumps
from api.demoQABaseClient.base_client import BaseClient
from demoQAUtils.data import DemoQA
from demoQAUtils.urls import Bookstore
from api.demoQABaseAPI.request import APIRequest
from demoQAUtils.book_selection import BookSelection


ISBN = BookSelection.select_a_book()


class BooksClient(BaseClient):
    def __init__(self):
        super().__init__()
        
        self.books_url = Bookstore.BOOKS
        self.single_book_url = Bookstore.SINGLE_BOOK
        self.selected_book_url = Bookstore.SELECTED_BOOK
        self.searched_book_url = Bookstore.SELECTION
        self.request = APIRequest()
        
    def get_all_books(self):
        return self.request.get(self.books_url)
    
    def get_searched_book(self):
        return self.request.get(self.searched_book_url)
    
    def get_selected_book(self):
        return self.request.get(self.selected_book_url)
    
    def add_books(self):
        payload = dumps(DemoQA.bookCollection)
        return self.request.post(self.books_url, payload, self.headers)
    
    def update_a_book(self):
        payload = dumps({"userId": DemoQA.userId, "isbn": "9712434961101"})
        return self.request.put(self.books_url+f"/{ISBN}", payload, self.headers)
    
    def partially_update_a_book(self):
        payload = dumps({"userId": DemoQA.userId, "isbn": "9578984058653"})
        return self.request.patch(self.books_url+f"/{ISBN}", payload, self.headers)
        
    def delete_a_book(self):
        payload = dumps({"userId": DemoQA.userId, "isbn": f"{ISBN}"})
        return self.request.delete(self.single_book_url, payload, self.headers)
    
    def delete_all_books(self):
        payload = dumps({"userId": DemoQA.userId})
        return self.request.delete(self.books_url, payload, self.headers)