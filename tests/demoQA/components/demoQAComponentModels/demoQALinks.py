from components.demoQAComponentLocators.pageElements import LinksLocators
from playwright.sync_api import expect


class LinksPage:
    def __init__(self, page):
        self.page = page
        self.pageHeader = page.locator(LinksLocators.PAGE_HEADER)
        self.apiResponse = page.locator(LinksLocators.MSG)
        
    def checkUI(self, linkText):
        pageHeaderCopy = 'Links'
        expect(self.pageHeader).to_be_visible()
        expect(self.pageHeader).to_contain_text(pageHeaderCopy)
    
    def checkLink(self, linkText, linkID, apiRespMsg):
        link = self.page.get_by_text(f"{linkText}")
        
        expect(link).to_be_visible()
        expect(link).to_be_enabled()
        expect(link).to_contain_text(f"{linkText}")
        expect(link).to_have_id(linkID)
        
        link.click()
        expect(self.apiResponse).to_be_visible()
        expect(self.apiResponse).to_contain_text(apiRespMsg)
        
    