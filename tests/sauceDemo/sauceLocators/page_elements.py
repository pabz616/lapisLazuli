
class SauceDemoPageLocators(object):
    PAGE_HEADING = '[class="login_logo"]'
    USN_INPUT = '[id="user-name"]'
    PWD_INPUT = '[id="password"]'
    SUBMIT_BTN = '[id="login-button"]'
    
class SwagLabsPageLocators(object):
    PAGE_HEADING = '[class="title"]'
    MENU_BUTTON = '[id="react-burger-menu-btn"]'
    CART_BUTTON = '[id="shopping_cart_container"]'
    
class SwagLabsMenuLocators(object):
    VIEW_ALL_ITEMS = '[id="inventory_sidebar_link"]'
    VIEW_ABOUT = '[id="about_sidebar_link"]'
    LOGOUT_LINK = '[id="logout_sidebar_link"]'
    RESET_APP = '[id="reset_sidebar_link"]'
    CLOSE_MENU = '[id="react-burger-cross-btn"]'
    
class SwagLabsProductsPageLocators(object):
    PRD1 = '[class="inventory_item"]'
    PRD1_IMG = '[src="/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"]'
    PRD1_IMG_LNK = '[id="item_4_img_link"]'
    PRD1_IMG_ALT = 'Sauce Labs Backpack'
    PRD1_NAME = '[class="inventory_item_name"]'    
    PRD1_DESC = '[class="inventory_item_desc"]'
    PRD1_PRICE = '[class="inventory_item_price"]'    
    PRD1_BTN = '[id="add-to-cart-sauce-labs-backpack"]'
    
    PRD2 = '(//div[@class="inventory_item"])[2]'
    PRD3 = '(//div[@class="inventory_item"])[3]'
    PRD4 = '(//div[@class="inventory_item"])[4]'
    PRD5 = '(//div[@class="inventory_item"])[5]'
    PRD6 = '(//div[@class="inventory_item"])[6]'
    
class SwagLabsCheckoutPageLocators(object):
    SECTION_TITLE = '#'
    QTY = '#'
    NAME = '#'
    DESC = '#'
    PRICE = '#'
    REMOVE_BTN = '#'
    CONTINUE_SHOPPING = '#'
    CHECKOUT_BTN = '[id="checkout"]'
    
class SwagLabsCustomerInfoPageLocators(object):
    SECTION_TITLE = '#'
    FNAME_INPUT = '[id="first-name"]'
    LNAME_INPUT = '[id="last-name"]'
    ZIP_INPUT = '[id="postal-code"]'
    CONTINUE_BUTTON = '[id="continue"]'
    CANCEL_BUTTON = '[id="cancel"]'
    
class SwagLabsOverviewPageLocators(object):
    SECTION_TITLE = '#'
    QTY = '#'
    NAME = '#'
    DESC = '#'
    PRICE = '#'
    PAYMENT_INFO = '#'
    SHIPPING_INFO = '#'
    PRICE_TOTAL =  '#'
    ITEM_TOTAL = '#'
    TAX = '#'
    TOTAL = '#'
    FINISH_BUTTON = '[id="finish"]'
    
class SwagLabsOrderConfirmationPageLocators(object):
    SECTION_TITLE = '[class="title"]'
    IMG = '[class="pony_express"]'
    MSG = '[class="complete-header"]'
    COPY = '[class="complete-text"]'
    BTN = '[id="back-to-products"]'    
    
class SwagLabsFooterLocators(object):
    pass
