"""
TEST BOOKS ENDPOINT
"""

import pytest
import json
from api.demoQAClient.book_client import BooksClient
from api.demoQAAssertions import assertions as confirm

client = BooksClient()


@pytest.mark.critical
@pytest.mark.api
class TestCriticalBookStoreEndpoints:
    def test_books_schema(self):
        response = client.get_all_books()
        data = json.loads(response.text)
        confirm.ok_response_status(response, 200)
        confirm.bookstore_catalog_schema(data)
        
    def test_select_a_book(self):
        response = client.get_selected_book()
        data = json.loads(response.text)
        confirm.ok_response_status(response, 200)
        confirm.selected_book_values(data)
        confirm.api_response_time


@pytest.mark.high
@pytest.mark.api
class TestHighBookStoreEndpoints:
    def test_add_new_books_as_unauthorized_user(self):
        response = client.add_books()
        confirm.unauthorized_status(response, 401)
        confirm.api_response_time
   
    def test_update_selected_book_as_unauthorized_user(self):
        response = client.update_a_book()
        confirm.unauthorized_status(response, 401)
        confirm.api_response_time
        
    def test_partial_update_of_selected_book_as_unauthorized_user(self):
        response = client.partially_update_a_book()
        confirm.not_found_response_status(response, 404)
        confirm.api_response_time
    
    def test_delete_selected_book_as_unauthorized_user(self):
        response = client.delete_a_book()
        confirm.unauthorized_status(response, 401)
        confirm.api_response_time
    
    def test_delete_all_books_as_unauthorized_user(self):
        response = client.delete_all_books()
        confirm.unauthorized_status(response, 401)
        confirm.api_response_time