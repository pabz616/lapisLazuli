from typing import Generator
from demoQAUtils.urls import RestFulBookerEndpoints as ep
from demoQAUtils.data import APIDemoData
import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.mark.api
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, ) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url=ep.RFB_URL, extra_http_headers=APIDemoData.HEADERS)
    yield request_context
    request_context.dispose()


# GET
def test_get_all_bookings(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get(ep.BOOKINGS)
    assert response.ok


def test_get_single_booking(api_request_context: APIRequestContext) -> None:
    single_booking_resp = api_request_context.get(ep.RANDOM_BOOKING_ID)
    assert single_booking_resp.ok


# POST    
def test_create_new_booking(api_request_context: APIRequestContext) -> None:
    new_booking_resp = api_request_context.post(ep.BOOKINGS, data=APIDemoData.BOOKING_DETAILS)
    assert new_booking_resp.ok
    
    # CHECK THE PRESENCE OF THE RESERVATION
    all_bookings = api_request_context.get(ep.BOOKINGS)
    assert all_bookings.ok


def test_create_new_admin(api_request_context: APIRequestContext) -> None:
    new_admin_resp = api_request_context.post(ep.AUTH_URL, data=APIDemoData.AUTH_DETAILS)
    assert new_admin_resp.ok
    
    token = new_admin_resp.json()
    assert len(token) != 0


# UPDATE - PUT
def test_update_booking(api_request_context: APIRequestContext) -> None:
    update_booking_resp = api_request_context.put(ep.SINGLE_BOOKING_ID, data=APIDemoData.DEFAULT_DETAILS)
    assert update_booking_resp.ok


# UPDATE - PATCH
def test_partially_update_booking(api_request_context: APIRequestContext) -> None:
    booking_details = {'additionalneeds': 'more drinks please'}
    
    # PARTIALLY UPDATE THE RESERVATION
    patch_booking_resp = api_request_context.patch(ep.SINGLE_BOOKING_ID, data=booking_details)
    assert patch_booking_resp.ok


# DELETE
def test_delete_booking(api_request_context: APIRequestContext) -> None:
    deleted_booking_resp = api_request_context.delete(ep.SINGLE_BOOKING_ID)
    assert deleted_booking_resp.ok