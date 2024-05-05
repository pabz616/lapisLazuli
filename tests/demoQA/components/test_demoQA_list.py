import pytest
from playwright.sync_api import Page
from demoQAComponent.demoQAList import ListPage
from demoQAUtils.data import ProjectData


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    listPageUrl = ProjectData.baseUrl+'/sortable'
    page.goto(listPageUrl)
    yield
    
    
@pytest.mark.normal
def test_list_sortable_UI(page: Page):
    """Test that entire list/grid page is to spec"""
    onListPage = ListPage(page)
    onListPage.checkUI

    
@pytest.mark.normal
def test_list_sort_rows(page: Page):
    """Test that the row for list/grid page is sorted after drag to a new row"""
    
    onListPage = ListPage(page)
    onListPage.sort_list
    onListPage.confirm_list_was_sorted