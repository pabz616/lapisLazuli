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
    productsTitle = 'Products'
    PRD1_IMG_URL = '/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg'
    PRD1_NAME = 'Sauce Labs Backpack'
    PRD1_PRICE = '$29.99'
    PRD2_IMG_URL = '#'
    PRD3_IMG_URL = '#'
    PRD4_IMG_URL = '#'
    PRD5_IMG_URL = '#'
    PRD6_IMG_URL = '#'

class SauceDemoCart(object):
    cartURL = 'cart.html'
class SauceDemoCheckout(object):
    orderCheckoutURL = 'checkout-step-one.html'
class SauceDemoOverview(object):
    orderOverviewURL = 'checkout-step-two.html'
class SauceDemoConfirmation(object):
    orderConfirmationURL = 'checkout-complete.html'
    
    successImageAlt = 'Pony Express'
    
    successMessage = 'Thank you for your order!'
    successCopy = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    