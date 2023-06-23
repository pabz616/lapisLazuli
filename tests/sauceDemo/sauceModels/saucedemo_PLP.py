from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.pageTitle = page.locator(SwagLabsPLPLocators.HEADER)
        self.product = page.locator(SwagLabsPLPLocators.PRD1).first
        self.product_image = page.locator(SwagLabsPLPLocators.PRD1_IMG).first
        self.product_name = page.locator(SwagLabsPLPLocators.PRD1_NAME).first
        self.product_description = page.locator(SwagLabsPLPLocators.PRD1_DESC).first
        self.product_price = page.locator(SwagLabsPLPLocators.PRD1_PRICE).first
        self.addToCartBtn = page.locator(SwagLabsPLPLocators.PRD1_BTN).first
        self.product_sort = page.locator(SwagLabsPLPLocators.PRD_SORT)        
        # ALL THE PRODUCTS
        self.item1 = page.locator(("//button[contains(.,'Add to cart')]")).locator("nth=0")
        self.item2 = page.locator(("//button[contains(.,'Add to cart')]")).locator("nth=1")
        self.item3 = page.locator(("//button[contains(.,'Add to cart')]")).locator("nth=-4")
        self.item4 = page.locator(("//button[contains(.,'Add to cart')]")).locator("nth=-3")
        self.item5 = page.locator(("//button[contains(.,'Add to cart')]")).locator("nth=-2")
        self.item6 = page.locator(("//button[contains(.,'Add to cart')]")).locator("nth=-1")
        
        self.cartBtn = page.locator(SwagLabsHeaderLocators.CART_BUTTON)
        self.itemAddedBadge = page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)
        
    def checkUI(self):
        self.pageTitle.is_visible()
        expect(self.product).to_be_visible()
        expect(self.product_image).to_be_visible()
        expect(self.product_name).to_be_visible()
        expect(self.product_description).to_be_visible()
        expect(self.product_price).to_be_visible()
        expect(self.addToCartBtn).to_be_visible()

    def addToCart(self):
        expect(self.cartBtn).to_be_visible()
        expect(self.cartBtn).to_be_enabled()
        
        self.addToCartBtn.click()

    def addAllItemsToCart(self):
        self.item1.click()
        self.item2.click()
        self.item3.click()
        self.item4.click()
        self.item5.click()
        self.item6.click()
        
        expect(self.itemAddedBadge).to_be_visible()
        expect(self.itemAddedBadge).to_have_text("6")

    def selectItem(self):
        self.product_name.click()
        
    def navigateToCartPage(self):
        self.cartBtn.click()

    def sortByProductNameAToZ(self):
        """THIS IS DEFAULT"""
        pass
        
    def sortByProductNameZToA(self):
        self.product_sort.select_option("za")
    
    def sortByProductPriceLowToHigh(self):
        self.product_sort.select_option("lohi")
        expect(self.product_name).to_be_visible()
        expect(self.product_price).to_have_text("$7.99")

    def sortByProductPriceHighToLow(self):
        self.product_sort.select_option("hilo")
        expect(self.product_name).to_be_visible()
        expect(self.product_price).to_have_text("$49.99")
        