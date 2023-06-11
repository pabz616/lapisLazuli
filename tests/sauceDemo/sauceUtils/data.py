class SauceDemoData(object):
    pageTitle = 'Swag Labs'
    sauceURL = 'https://www.saucedemo.com/'
    password = 'secret_sauce'
    validUSN = 'standard_user'
    lockedOutUSN = 'locked_out_user'
    problemUSN = 'problem_user'
    glitchedUSN = 'performance_glitch_user'
class SauceDemoProducts(object):   
    productsURL = SauceDemoData.sauceURL+'inventory.html'
    selectedItemURL = SauceDemoData.sauceURL+'inventory-item.html?id=4'
    productsTitle = 'Products'
    PRD1_IMG_URL = '/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg'
    PRD1_NAME = 'Sauce Labs Backpack'
    PRD1_PRICE = '$29.99'
    PRD2_IMG_URL = '#'
    PRD3_IMG_URL = '#'
    PRD4_IMG_URL = '#'
    PRD5_IMG_URL = '#'
    PRD6_IMG_URL = '#'
    NO_ITEM = 'ITEM NOT FOUND'
    NO_ITEM_COPY = "We're sorry, but your call could not be completed as dialled. Please check your number, and try your call again. If you are in need of assistance, please dial 0 to be connected with an operator. This is a recording. 4 T 1."

class SauceDemoCart(object):
    cartURL = 'cart.html'
    cartPageTitle = 'Your Cart'
    cartItem = 'Sauce Labs Backpack'
    cartItemPrice = '$29.99'
    cartQtyLabel = 'QTY'
    cartDescriptionLabel = 'Description'
    cartItemCopy = 'Carry all the things with the sleek, streamlined sly pack that melds uncompromising style with unequaled laptop and tablet protection.'
    cartRemoveItemBtnText = 'Remove'
    cartCheckoutBtnText = 'Checkout'
    cartContinueBtnText = 'Continue Shopping'
class SauceDemoCheckout(object):
    orderCheckoutURL = SauceDemoData.sauceURL+'checkout-step-one.html'
class SauceDemoOverview(object):
    orderOverviewURL = 'checkout-step-two.html'
class SauceDemoConfirmation(object):
    orderConfirmationURL = 'checkout-complete.html'
    
    successImageAlt = 'Pony Express'
    
    successMessage = 'Thank you for your order!'
    successCopy = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    