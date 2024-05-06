from components.demoQAComponentLocators.pageElements import RadioButtonLocators
from playwright.sync_api import expect


class RadioButtonPage:
    def __init__(self, page):
        self.page = page
        self.pageHeader = page.locator(RadioButtonLocators.PAGE_HEADER)
        
        self.radioBtnQuestion = page.locator(RadioButtonLocators.RB_QUESTION)
        
        self.yes_radioBtnLabel = page.locator(RadioButtonLocators.RB_ANSWER1_LABEL)
        self.yes_radioBtn = page.get_by_label('yesRadio')  # page.locator(RadioButtonLocators.RB_ANSWER1)
        
        self.impressive_radioBtnLabel = page.locator(RadioButtonLocators.RB_ANSWER2_LABEL)
        self.impressive_radioBtn = page.locator(RadioButtonLocators.RB_ANSWER2)
        
        self.no_radioBtnLabel = page.locator(RadioButtonLocators.RB_ANSWER3_LABEL)
        self.no_radioBtn = page.locator(RadioButtonLocators.RB_ANSWER3)
        
        self.message_element = page.locator(RadioButtonLocators.MSG)
    
    def checkUI(self):
        pageHeaderCopy = 'Radio Button'
        questionLabelCopy = 'Do you like the site?'
       
        expect(self.pageHeader).to_be_visible()
        expect(self.pageHeader).to_contain_text(pageHeaderCopy)
        #
        expect(self.radioBtnQuestion).to_be_visible()
        expect(self.radioBtnQuestion).to_contain_text(questionLabelCopy)
        #
        expect(self.yes_radioBtn).to_be_visible()
        expect(self.yes_radioBtn).not_to_be_disabled()
        
        expect(self.impressive_radioBtn).to_be_visible()
        expect(self.impressive_radioBtn).not_to_be_disabled()
        
        expect(self.no_radioBtn).to_be_visible()
        expect(self.no_radioBtn).not_to_be_disabled()
        
    def selectYes(self):
        self.yes_radioBtn.check()

    def selectImpressive(self):
        self.impressive_radioBtn.click()
    
    def selectNo(self):
        self.no_radioBtn.click()
    
    def checkMessage(self, message):
        expect(self.message_element).to_be_visible()
        expect(self.message_element).to_contain_text(message)
        
        
