import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd
from demoQAComponentModels.demoQADatePicker import DatePickerPage

from faker import Faker
fake = Faker()


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.normal
# use --browser-channel "chrome" to run tests in chrome, not chromium
class TestDatePicker:
    
    def before_each(page: Page):
        DatePickerUrl = pd.baseUrl+'/date-picker'
        page.goto(DatePickerUrl)
        yield
        
    def test_datepicker_UI(page: Page):
        """Test that entire datepicker page is to spec"""
        
        onDatePickerPage = DatePickerPage(page)
        onDatePickerPage.checkUI
        
    def test_datepicker_add_date(page: Page):
        """Test that a valid date can be entered in the datepicker"""
        
        onDatePickerPage = DatePickerPage(page)
        onDatePickerPage.enterDate(fake.date())
        onDatePickerPage.confirmDateEntered

    def test_datepicker_add_date_and_time(page: Page):
        """Test that a valid date and time can be entered in the datepicker that features a timestamp"""
    
        month = fake.month_name()
        day = fake.day_of_month()
        year = fake.year()
        
        dateTimeCopy = month+''+day+''+year+'5:00 PM'
        
        onDatePickerPage = DatePickerPage(page)
        onDatePickerPage.enterDateAndTime(dateTimeCopy)
        onDatePickerPage.confirmDateTineEntered