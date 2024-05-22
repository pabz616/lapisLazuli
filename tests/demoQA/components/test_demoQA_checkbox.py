import pytest
from playwright.sync_api import Page
from utils.data import DemoQA
from components.demoQAComponentModels.demoQACheckBox import CheckBoxPage


@pytest.mark.normal
class TestCheckboxes:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        checkBoxPageUrl = DemoQA.baseUrl+'/checkbox'
        page.goto(checkBoxPageUrl)
        yield

    def test_checkbox_UI(self, page: Page):
        """Test that entire checkbox page is to spec"""
           
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.checkUI

    def test_checkbox_display_selection_message(self, page: Page):
        """Test to display list of subdirectories""" 
        
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.displayMessage

    def test_checkbox_hide_selection_message(self, page: Page):
        """Test to hide list of subdirectories"""
        
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.hideMessage
        
    def test_checkbox_expand_home_directory(self, page: Page):
        """Test to expand home directory and display subdirectories"""
        
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.expandHomeDirectory
        onCheckBoxPage.confirmDisplayOfHomeSubDirectories
        
    def test_checkbox_expand_desktop_subdirectories(self, page: Page):
        """Test to expand home directory, desktop subdirectory and display its subdirectories"""
        
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.expandHomeDirectory
        onCheckBoxPage.expandDesktopDirectory
        onCheckBoxPage.confirmDisplayOfDesktopSubdirectories
    
    def test_checkbox_expand_all_subdirectories(self, page: Page):
        """Test to expand all corresponding subdirectories for home, desktop, documents, and downloads"""
        
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.expandAllDirectories
        onCheckBoxPage.confirmDisplayOfAllSubDirectories
        
    def test_checkbox_hide_all_subdirectories(self, page: Page):
        """Test to collapse all corresponding subdirectories"""
        
        onCheckBoxPage = CheckBoxPage(page)
        onCheckBoxPage.expandAllDirectories
        onCheckBoxPage.collapseAllDirectories
        onCheckBoxPage.confirmSubDirectoriesAreHidden