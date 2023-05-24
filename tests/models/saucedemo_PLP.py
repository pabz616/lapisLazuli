from locators.page_elements import *

class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.pageTitle = page.locator(SwagLabsPageLocators.PAGE_HEADING)
        # More Locators here
        
    def checkUI(self):
        self.pageTitle.is_visible()
        # 
        #TODO loop through all products:
        # check product image (ref. alt tag)
        # check product title
        # check product description
        # check product price
        # check add-to-cart button
        