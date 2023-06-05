from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.pageTitle = page.locator(SwagLabsPageLocators.PAGE_HEADING)
        self.product = page.locator(SwagLabsProductsPageLocators.PRD1).first
        self.product_image = page.locator(SwagLabsProductsPageLocators.PRD1_IMG).first
        self.product_name = page.locator(SwagLabsProductsPageLocators.PRD1_NAME).first
        self.product_description = page.locator(SwagLabsProductsPageLocators.PRD1_DESC).first
        self.product_price = page.locator(SwagLabsProductsPageLocators.PRD1_PRICE).first
        self.addToCartBtn = page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first
        self.cartBtn = page.locator(SwagLabsPageLocators.CART_BUTTON)
        
    def checkUI(self):
        self.pageTitle.is_visible()
        expect(self.product).to_be_visible()
        expect(self.product_image).to_be_visible()
        expect(self.product_name).to_be_visible()
        expect(self.product_description).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.addToCartBtn).to_be_visible()
           
        # 
        #TODO loop through all products:
        # check product image (ref. alt tag)
        # check product title
        # check product description
        # check product price
        # check add-to-cart button

    def addToCart(self):
        expect(self.cartBtn).to_be_visible()
        expect(self.cartBtn).to_be_enabled()
        
        self.addToCartBtn.click()
    
    def navigateToCartPage(self):
        self.cartBtn.click()
        
        
        