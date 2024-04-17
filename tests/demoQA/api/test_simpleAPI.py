from typing import Generator
from utils.data import APIDemoData

import pytest
from playwright.sync_api import Playwright, APIRequestContext

BOOKINGID = 2


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, ) -> Generator[APIRequestContext, None, None]:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }
    request_context = playwright.request.new_context(base_url=APIDemoData.BOOKER_URL, extra_http_headers=headers)
    yield request_context
    request_context.dispose()


#  GET
@pytest.mark.api
def test_get_all_bookings(api_request_context: APIRequestContext) -> None:
    booking_resp = api_request_context.get(APIDemoData.BOOKER_URL+"/booking")
    assert booking_resp.ok


@pytest.mark.api
def test_get_single_booking(api_request_context: APIRequestContext) -> None:
    single_booking_resp = api_request_context.get(APIDemoData.BOOKER_URL+f"/booking/{BOOKINGID}")
    assert single_booking_resp.ok


# POST    
@pytest.mark.api
def test_create_new_booking(api_request_context: APIRequestContext) -> None:
    booking_details = {
        'firstname': 'Jon',
        'lastname': 'Snow',
        'totalprice': 747,
        'depositpaid': True,
        'bookingdates': {
            'checkin' : '2023-06-01',
            'checkout' : '2023-07-01'
        },
        'additionalneeds': "dragon glass"
    }
    
    # CREATE THE RESERVATION
    new_booking = api_request_context.post(APIDemoData.BOOKER_URL+"/booking", data=booking_details)
    assert new_booking.ok
    
    booking_response = new_booking.json()
    print(f"this is my new booking: {booking_response}")

    # CHECK THE PRESENCE OF THE RESERVATION
    all_bookings = api_request_context.get(APIDemoData.BOOKER_URL)
    assert all_bookings.ok


@pytest.mark.api
def test_create_new_admin(api_request_context: APIRequestContext) -> None:
    auth_details = {
        'username': 'admin',
        'password': 'password123'
    }
    
    # CREATE THE RESERVATION
    new_admin = api_request_context.post(APIDemoData.BOOKER_URL+"/auth", data=auth_details)
    assert new_admin.ok
    
    token = new_admin.json()
    print(f"my new token: {token}")


# UPDATE - PUT
def test_update_booking(api_request_context: APIRequestContext) -> None:
    booking_details = {
        'firstname': 'Sally',
        'lastname': 'Brown',
        'totalprice': 747,
        'depositpaid': True,
        'bookingdates': {
            'checkin' : '2023-07-01',
            'checkout' : '2023-07-30'
        },
        'additionalneeds': "furry pillows"
    }
    
    # UPDATE THE RESERVATION
    update_booking = api_request_context.put(APIDemoData.BOOKER_URL+f"/booking/{BOOKINGID}", data=booking_details)
    assert update_booking.ok

        
# UPDATE - PATCH
def test_partially_update_booking(api_request_context: APIRequestContext) -> None:
    booking_details = {
        'firstname': 'Sally',
        'lastname': 'Brown',
        'additionalneeds': 'more drinks please'
    }
    
    # PARTIALLY UPDATE THE RESERVATION
    patch_booking = api_request_context.patch(APIDemoData.BOOKER_URL+f"/booking/{BOOKINGID}", data=booking_details)
    assert patch_booking.ok


# DELETE
def test_delete_booking(api_request_context: APIRequestContext) -> None:
    deleted_booking = api_request_context.delete(APIDemoData.BOOKER_URL+f"/booking/{BOOKINGID}")
    assert deleted_booking.ok