
class SauceDemoPageLocators(object):
    SAUCE_LOGO = '[class="login_logo"]'
    USN_INPUT = '[id="user-name"]'
    PWD_INPUT = '[id="password"]'
    SUBMIT_BTN = '[id="login-button"]'
    SECTION_TITLE = '[class="title"]'
    
class SwagLabsHeaderLocators(object):
    HEADER_LOGO = '[class="app_logo"]'
    PAGE_HEADING = '[class="title"]'
    MENU_BUTTON = '[id="react-burger-menu-btn"]'
    CART_BUTTON = '[id="shopping_cart_container"]'
    ITEM_ADDED_BADGE = '[class="shopping_cart_badge"]'
    
class SwagLabsMenuLocators(object):
    VIEW_ALL_ITEMS = '[id="inventory_sidebar_link"]'
    VIEW_ABOUT = '[id="about_sidebar_link"]'
    LOGOUT_LINK = '[id="logout_sidebar_link"]'
    RESET_APP = '[id="reset_sidebar_link"]'
    CLOSE_MENU = '[id="react-burger-cross-btn"]'
    
class SwagLabsProductsPageLocators(object):
    HEADER = SauceDemoPageLocators.SECTION_TITLE
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
    PRD1_BTN = '[class="btn btn_primary btn_small btn_inventory"]'
    PRD1_REMOVE = '[class="btn btn_secondary btn_small btn_inventory"]'

class SwagLabsPDPLocators(object):
    PRD_IMG = '[class="inventory_details_img"]'
    PRD_NAME = '[class="inventory_details_name large_size"]'    
    PRD_DESC = '[class="inventory_details_desc large_size"]'
    PRD_PRICE = '[class="inventory_details_price"]'    
    PRD_BTN = '[class="btn btn_primary btn_small btn_inventory"]'
    
    
class SwagLabsCartPageLocators(object):
    SECTION_TITLE = SauceDemoPageLocators.SECTION_TITLE
    QTY_LABEL = '[class="cart_quantity_label"]'
    QTY_INPUT = '[class="cart_quantity"]'
    DESC_LABEL = '[class="cart_desc_label"]'
    NAME = '[class="inventory_item_name"]'
    DESC = '[class="inventory_item_desc"]'
    PRICE = '[class="inventory_item_price"]'
    REMOVE_BTN = '[class="btn btn_secondary btn_small cart_button"]'
    CONTINUE_SHOPPING = '[class="btn btn_secondary back btn_medium"]'
    CHECKOUT_BTN = '[class="btn btn_action btn_medium checkout_button"]'
    
class SwagLabsCheckoutPageLocators(object):
    SECTION_TITLE = SauceDemoPageLocators.SECTION_TITLE
    FNAME_INPUT = '[id="first-name"]'
    LNAME_INPUT = '[id="last-name"]'
    ZIP_INPUT = '[id="postal-code"]'
    CONTINUE_BUTTON = '[id="continue"]'
    CANCEL_BUTTON = '[id="cancel"]'
    ERROR_ICON = '[class="svg-inline--fa fa-times-circle fa-w-16 error_icon"]'
    ERROR_MSG = '[class="error-message-container error"]'
    
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
