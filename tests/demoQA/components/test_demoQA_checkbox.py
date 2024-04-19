import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd

from demoQAModels.demoQACheckBox import CheckBoxPage


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    checkBoxPageUrl = pd.baseUrl+'/checkbox'
    page.goto(checkBoxPageUrl)
    yield


@pytest.mark.normal
def test_checkbox_UI(page: Page):
    """Test that entire checkbox page is to spec"""
    
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.checkUI


@pytest.mark.normal
def test_checkbox_display_selection_message(page: Page):
    """Test to display list of subdirectories"""
    
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.displayMessage


@pytest.mark.normal
def test_checkbox_hide_selection_message(page: Page):
    """Test to hide list of subdirectories"""
    
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.hideMessage
    
    
@pytest.mark.normal
def test_checkbox_expand_home_directory(page: Page):
    """Test to expand home directory and display subdirectories"""
    
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.expandHomeDirectory
    onCheckBoxPage.confirmDisplayOfHomeSubDirectories
    
    
@pytest.mark.normal
def test_checkbox_expand_desktop_subdirectories(page: Page):
    """Test to expand home directory, desktop subdirectory and display its subdirectories"""
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.expandHomeDirectory
    onCheckBoxPage.expandDesktopDirectory
    onCheckBoxPage.confirmDisplayOfDesktopSubdirectories
  
    
@pytest.mark.normal
def test_checkbox_expand_all_subdirectories(page: Page):
    """Test to expand all corresponding subdirectories for home, desktop, documents, and downloads"""
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.expandAllDirectories
    onCheckBoxPage.confirmDisplayOfAllSubDirectories
    
    
@pytest.mark.normal
def test_checkbox_hide_all_subdirectories(page: Page):
    """Test to collapse all corresponding subdirectories"""
    onCheckBoxPage = CheckBoxPage(page)
    onCheckBoxPage.expandAllDirectories
    onCheckBoxPage.collapseAllDirectories
    onCheckBoxPage.confirmSubDirectoriesAreHidden