from demoQAComponentLocators.pageElements import TextFormLocators
from playwright.sync_api import expect


class TextBoxPage:
    def __init__(self, page):
        self.page = page
        self.pageHeader = page.locator(TextFormLocators.PAGE_HEADER)       
        self.nameFieldLabel = page.locator(TextFormLocators.FULLNAME_INPUT_LABEL)
        self.nameField = page.locator(TextFormLocators.FULLNAME_INPUT)
        
        self.emailFieldLabel = page.locator(TextFormLocators.EMAIL_INPUT_LABEL)
        self.emailField = page.locator(TextFormLocators.EMAIL_INPUT)
        self.emailFieldError = page.locator(TextFormLocators.EMAIL_INPUT_ERROR)

        self.currentAddressFieldLabel = page.locator(TextFormLocators.ADDRESS_INPUT_LABEL)
        self.currentAddressField = page.locator(TextFormLocators.ADDRESS_INPUT)

        self.permanentAddressFieldLabel = page.locator(TextFormLocators.PERM_ADDRESS_INPUT_LABEL)
        self.permanentAddressField = page.locator(TextFormLocators.PERM_ADDRESS_INPUT)

        self.submitButton = page.locator(TextFormLocators.SUBMIT_BUTTON)
        
        self.resultsPanel = page.locator(TextFormLocators.RESULTS_OUTPUT)
                   
    def checkUI(self):
        pageHeaderCopy = 'Text Box'
        nameInputLabelCopy = 'Full Name'
        emailInputLabelCopy = 'Email'
        addressInputLabelCopy = 'Current Address'
        permanentAddressInputLabelCopy = 'Permanent Address'
        
        expect(self.pageHeader).to_be_visible()
        expect(self.pageHeader).to_contain_text(pageHeaderCopy)
        #
        expect(self.nameFieldLabel).to_be_visible()
        expect(self.nameFieldLabel).to_contain_text(nameInputLabelCopy)
        expect(self.nameField).to_be_visible()
        expect(self.nameField).to_be_empty()
        #
        expect(self.emailFieldLabel).to_be_visible()
        expect(self.emailFieldLabel).to_contain_text(emailInputLabelCopy)
        expect(self.emailField).to_be_visible()
        expect(self.emailField).to_be_empty()
        #
        expect(self.currentAddressFieldLabel).to_be_visible()
        expect(self.currentAddressFieldLabel).to_contain_text(addressInputLabelCopy)
        expect(self.currentAddressField).to_be_visible()
        expect(self.currentAddressField).to_be_empty()
        #
        expect(self.permanentAddressFieldLabel).to_be_visible()
        expect(self.permanentAddressFieldLabel).to_contain_text(permanentAddressInputLabelCopy)
        expect(self.permanentAddressField).to_be_visible()
        expect(self.permanentAddressField).to_be_empty()
        #
        expect(self.submitButton).to_be_visible()
        expect(self.submitButton).to_be_enabled()

    def fillForm(self, name, email, addr1, addr2):
        self.nameField.fill(name)
        self.emailField.fill(email)
        self.currentAddressField.fill(addr1)
        self.permanentAddressField.fill(addr2)
        self.submitButton.click()
    
    def confirmResult(self, name, email, addr1, addr2):
        expect(self.resultsPanel).to_be_visible()
        expect(self.resultsPanel).to_contain_text(name)
        expect(self.resultsPanel).to_contain_text(email)
        expect(self.resultsPanel).to_contain_text(addr1)
        expect(self.resultsPanel).to_contain_text(addr2)
    
    def confirmEmailInputErrorState(self):
        expect(self.emailFieldError).to_be_visible()