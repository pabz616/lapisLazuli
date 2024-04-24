"""
TEST BOOKS ENDPOINT
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd, DemoQA
from demoQAUtils.urls import Bookstore


@pytest.mark.critical
@pytest.mark.api
class TestCriticalBookStoreEndpoints:
    def test_books_schema(self):
        response = requests.get(Bookstore.BOOKS)
        resp = response.json()
        assert response.status_code == 200, 'Error: {0}'.format(response.status_code)
        assert len(resp) != 0
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
        # TEST KEYS
        assert "isbn" in resp["books"][0]
        assert "title" in resp["books"][0]
        assert "subTitle" in resp["books"][0]
        assert "author" in resp["books"][0]
        assert "publish_date" in resp["books"][0]
        assert "publisher" in resp["books"][0]
        assert "pages" in resp["books"][0]
        assert "description" in resp["books"][0]
        assert "website" in resp["books"][0]
    
    def test_books_results(self):
        response = requests.get(Bookstore.BOOKS)
        resp = response.json()
        assert response.status_code == 200, 'Error: {0}'.format(response.status_code)
        assert len(resp) != 0
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
        
        # TEST VALUES FOR FIRST BOOK
        assert resp["books"][0]["isbn"] == "9781449325862"
        assert resp["books"][0]["title"] == "Git Pocket Guide"
        assert resp["books"][0]["subTitle"] == "A Working Introduction"
        assert resp["books"][0]["author"] == "Richard E. Silverman"
        assert resp["books"][0]["publish_date"] == "2020-06-04T08:48:39.000Z"
        assert resp["books"][0]["publisher"] == "O'Reilly Media"
        assert resp["books"][0]["pages"] == 234
        assert resp["books"][0]["description"] is not None
        assert resp["books"][0]["website"] == "http://chimera.labs.oreilly.com/books/1230000000561/index.html"


@pytest.mark.high
@pytest.mark.api
class TestHighBookStoreEndpoints:
    def test_select_a_book(self):
        response = requests.get(Bookstore.SELECTED_BOOK)
        resp = response.json()
        
        # TEST RESPONSE
        assert response.status_code == 200, 'Error: {0}'.format(response.status_code)
        assert len(resp) != 0
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
        
        # TEST RESPONSE VALUES 
        assert resp["isbn"] is not None
        assert resp["title"] == "Designing Evolvable Web APIs with ASP.NET"
        assert resp["subTitle"] == "Harnessing the Power of the Web"
        assert resp["author"] == "Glenn Block et al."
        assert resp["publish_date"] == "2020-06-04T09:12:43.000Z"
        assert resp["publisher"] == "O'Reilly Media"
        assert resp["pages"] == 238
        assert resp["description"] is not None
        assert resp["website"] == "http://chimera.labs.oreilly.com/books/1234000001708/index.html"

    def test_add_new_books_as_unauthorized_user(self):
        response = requests.post(Bookstore.BOOKS, json=DemoQA.bookCollection)
        assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)

    def test_delete_books_as_unauthorized_user(self):
        response = requests.delete(Bookstore.BOOKS, json=DemoQA.userData)
        assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
         
    def test_update_selected_book_as_unauthorized_user(self):
        response = requests.put(f"{Bookstore.BOOKS}/9781449365035", json=DemoQA.bookData)
        assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)

    def test_partial_update_of_selected_book_as_unauthorized_user(self):
        response = requests.put(f"{Bookstore.BOOKS}/9781449365035", json=DemoQA.bookData)
        assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
    def test_delete_selected_book_as_unauthorized_user(self):
        response = requests.delete(Bookstore.SELECTED_BOOK, json=DemoQA.bookData)
        assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
