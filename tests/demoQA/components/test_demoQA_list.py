import pytest
from playwright.sync_api import Page
from components.demoQAComponentModels.demoQAList import ListPage
from utils.data import DemoQA


@pytest.mark.normal
class TestList:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        listPageUrl = DemoQA.baseUrl+'/sortable'
        page.goto(listPageUrl)
        yield
        
    def test_list_sortable_UI(self, page: Page):
        """Test that entire list/grid page is to spec"""
        
        onListPage = ListPage(page)
        onListPage.checkUI

    def test_list_sort_rows(self, page: Page):
        """Test that the row for list/grid page is sorted after drag to a new row"""
        
        onListPage = ListPage(page)
        onListPage.sort_list
        onListPage.confirm_list_was_sorted