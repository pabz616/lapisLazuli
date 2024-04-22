"""
TEST BOOKS ENDPOINT
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd

booksEndpoint = pd.baseUrl+'/BookStore/v1/Books'
selectedBookEndpoint = pd.baseUrl+'/BookStore/v1/Book?ISBN=9781449337711'
response_limit = float(1.0)
    

@pytest.mark.critical
@pytest.mark.api
def test_books_schema():
    response = requests.get(booksEndpoint)
    resp = response.json()
    assert response.status_code == 200, 'Error: {0}'.format(response.status_code)
    assert len(resp) != 0
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
  
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
    

@pytest.mark.critical
@pytest.mark.api    
def test_books_results():
    response = requests.get(booksEndpoint)
    resp = response.json()
    assert response.status_code == 200, 'Error: {0}'.format(response.status_code)
    assert len(resp) != 0
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
       
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
def test_add_new_books_as_unauthorized_user():
    data = {"userId": pd.demoQAUserId,
            "collectionOfIsbns:": [
                {"isbn": "9785303754511"},
                {"isbn": "9712434961101"},
                {"isbn": "9578984058653"},
                ]
            }
    response = requests.post(booksEndpoint, json=data)
    assert response.status_code != 201, "Bug! Unauthorized user can modify contents"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)


@pytest.mark.high
@pytest.mark.api
def test_delete_books_as_unauthorized_user():
    data = {"userId": pd.demoQAUserId}
    response = requests.delete(booksEndpoint, json=data)
    assert response.status_code != 204, "Bug! Unauthorized user can delete contents"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    

@pytest.mark.high
@pytest.mark.api    
def test_selected_book_result():
    response = requests.get(selectedBookEndpoint)
    resp = response.json()
    
    # TEST RESPONSE
    assert response.status_code == 200, 'Error: {0}'.format(response.status_code)
    assert len(resp) != 0
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
       
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
 
  
@pytest.mark.high
@pytest.mark.api
def test_update_selected_book_as_unauthorized_user():
    response = requests.put(booksEndpoint+'/9781449365035')
    assert response.status_code != 200, "Bug! Unauthorized user can update book"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)

    
@pytest.mark.high
@pytest.mark.api
def test_partial_update_of_selected_book_as_unauthorized_user():
    response = requests.patch(booksEndpoint+'/9781449365035')
    assert response.status_code != 200, "Bug! Unauthorized user can partially update book"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
    
@pytest.mark.high
@pytest.mark.api
def test_delete_selected_book_as_unauthorized_user():
    data = {"userId": pd.demoQAUserId, "isbn": "9781449331818"}
    response = requests.delete(selectedBookEndpoint, json=data)
    assert response.status_code != 201, "Bug! Unauthorized user can delete book"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)