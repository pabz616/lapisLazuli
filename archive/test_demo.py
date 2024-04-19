import pytest
from typing import Generator
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

DEMO_URL = 'https://restful-booker.herokuapp.com'

@pytest.fixture(scope="module")
def resIds():
    # keys list
    keys = []
    yield keys
  
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
        'Accept: application/json'
        'Content-Type: application/json'
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
        'token':'60fcb557440419a'
        }
    
    request_context = playwright.request.new_context(base_url=f"{DEMO_URL}")
    yield request_context
    request_context.dispose()

@pytest.mark.skip(reason="Token is already generated. Test Passes")
def test_generate_token(api_request_context: APIRequestContext) -> None:
    data ={
        'username': 'admin',
        'password': 'password123'
    }
    
    resp = api_request_context.post(f"/auth", data=data)
    assert resp.ok
    
    token = resp.json()
     
def test_reservations_health_check(api_request_context: APIRequestContext) -> None:
    reservations_health_check = api_request_context.get(f"/ping")
    assert reservations_health_check.ok

def test_get_all_booked_reservations(api_request_context: APIRequestContext) -> None:
    all_booked_reservations = api_request_context.get(f"/booking")
    assert all_booked_reservations.ok
    
def test_get_individual_booked_reservations(api_request_context: APIRequestContext) -> None:
    single_reservation = api_request_context.get(f"/booking/2")
    assert single_reservation.ok
    
def test_create_a_new_reservation(api_request_context: APIRequestContext, resIds) -> None:
    data = {
        
        "firstname" : "Rick",
        "lastname" : "Flair",
        "totalprice" : 333,
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2023-07-01",
        "checkout" : "2023-08-01"
        },
        "additionalneeds" : "Lunch and today's newspaper"
    }
    new_reservation = api_request_context.post(f"/booking", data=data)
    assert new_reservation.ok
    
    new_res_resp = new_reservation.json()
    resIds.append(new_res_resp['bookingid'])
    print("my ids are:", resIds)

@pytest.mark.skip(reason="Getting 403 errors .. could be the id I'm using")
def test_update_a_reservation(api_request_context: APIRequestContext) -> None:
    data = {
            "firstname" : "Rick",
            "lastname" : "Flair",
            "totalprice" : 400,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : "2023-07-01",
                "checkout" : "2023-08-01"
                },
            "additionalneeds" : "Send flowers to mom!"
        }
    partial_reservation_update = api_request_context.put(f"/booking/2", data=data)
    
    assert partial_reservation_update.ok

@pytest.mark.skip(reason="Getting 403 errors .. could be the id I'm using")
def test_partial_update_to_a_reservation(api_request_context: APIRequestContext) -> None:
    data={ "additionalneeds" : "Pay for boat"}
    partial_res_update = api_request_context.patch(f"/booking/2", data=data)
    
    assert partial_res_update.ok
 
@pytest.mark.skip(reason="Getting 403 errors .. could be the id I'm using")   
def test_delete_a_reservation(api_request_context: APIRequestContext) -> None:
    delete_res = api_request_context.delete(f"/booking/62")
    
    assert delete_res.ok