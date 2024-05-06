from components.demoQAComponentLocators.pageElements import DatePickerLocators
from playwright.sync_api import expect
from demoQAUtils.data import DemoQADates as testData


class DatePickerPage:
    def __init__(self, page):
        self.page = page
        self.pageHeader = page.locator(DatePickerLocators.PAGE_HEADER)
        self.datePickerInput = page.locator(DatePickerLocators.DATE)
        self.dateTimeInput = page.locator(DatePickerLocators.DATETIME)
            
    def checkUI(self):
        pageHeaderCopy = 'Date Picker'
        datePickerInputCopy = self.datePickerInput.textContent
        dateTimeInputCopy = self.dateTimeInput.textContent
    
        expect(self.pageHeader).to_be_visible()
        expect(self.pageHeader).to_contain_text(pageHeaderCopy)
        #
        expect(self.datePickerInput).to_be_visible()
        expect(self.datePickerInput).to_contain_text(datePickerInputCopy)
        #
        expect(self.dateTimeInput).to_be_visible()
        expect(self.dateTimeInput).to_contain_text(dateTimeInputCopy)
        
    def enterDate(self, sampleDate):
        self.datePickerInput.fill(sampleDate)
        
    def enterDateAndTime(self, dateTime):
        self.datePickerInput.fill(dateTime)

    def confirmDateEntered(self):
        expect(self.dateTimeInput).not_to_contain_text(testData.simpleDate)
        
    def confirmDateTineEntered(self):
        expect(self.dateTimeInput).not_to_contain_text(testData.simpleDate)
        

    