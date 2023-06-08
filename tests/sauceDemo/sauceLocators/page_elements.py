
class SauceDemoPageLocators(object):
    SAUCE_LOGO = '[class="login_logo"]'
    USN_INPUT = '[id="user-name"]'
    PWD_INPUT = '[id="password"]'
    SUBMIT_BTN = '[id="login-button"]'
    
class SwagLabsHeaderLocators(object):
    HEADER_LOGO = '[class="app_logo"]'
    PAGE_HEADING = '[class="title"]'
    MENU_BUTTON = '[id="react-burger-menu-btn"]'
    CART_BUTTON = '[id="shopping_cart_container"]'
    ITEM_ADDED_BADGE = '[span="shopping_cart_badge"]'
    
class SwagLabsMenuLocators(object):
    VIEW_ALL_ITEMS = '[id="inventory_sidebar_link"]'
    VIEW_ABOUT = '[id="about_sidebar_link"]'
    LOGOUT_LINK = '[id="logout_sidebar_link"]'
    RESET_APP = '[id="reset_sidebar_link"]'
    CLOSE_MENU = '[id="react-burger-cross-btn"]'
    
class SwagLabsProductsPageLocators(object):
    HEADER = '[class="title"]'
    PRD1 = '[class="inventory_item"]'
    SELECTED_OPTION = '[class="active_option"]'
    PRD_SORT = '[class="product_sort_container"]'
    PRD1_IMG_SRC = '[src="/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"]'
    PRD1_IMG = '[class="inventory_item_img"]'
    PRD1_IMG_LNK = '[id="item_4_img_link"]'
    PRD1_IMG_ALT = 'Sauce Labs Backpack'
    PRD1_NAME = '[class="inventory_item_name"]'    
    PRD1_DESC = '[class="inventory_item_desc"]'
    PRD1_PRICE = '[class="inventory_item_price"]'    
    PRD1_BTN = '[id="add-to-cart-sauce-labs-backpack"]'

class SwagLabsPDPLocators(object):
    PRD_IMG = '[class="inventory_details_img"]'
    PRD_NAME = '[class="inventory_details_name large_size"]'    
    PRD_DESC = '[class="inventory_details_desc large_size"]'
    PRD_PRICE = '[class="inventory_details_price"]'    
    PRD_BTN = '[class="btn btn_primary btn_small btn_inventory"]'
    
    
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
