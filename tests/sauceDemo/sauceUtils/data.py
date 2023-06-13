class SauceDemoData(object):
    pageTitle = 'Swag Labs'
    sauceURL = 'https://www.saucedemo.com/'
    password = 'secret_sauce'
    validUSN = 'standard_user'
    lockedOutUSN = 'locked_out_user'
    problemUSN = 'problem_user'
    glitchedUSN = 'performance_glitch_user'
    short_text = 'Lor'
    sample_text = 'Loremipsum'
    sample_number = '2123334455'
    sample_zip = '10010'
    short_number = '212'
    mixed_char = 'Lorem 123 $#@ ipsum dolor sit amet, Римский император Константин I Великий, 北京位於華北平原的西北边缘'
    alpha_num = 'awesom123'
    script = '<script>alert("this should be blocked")</script>'
    long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quisque non tellus orci ac auctor augue mauris augue. Sagittis orci a scelerisque purus semper. Neque sodales ut etiam sit amet nisl purus in mollis. Blandit libero volutpat sed cras. Sed lectus vestibulum mattis ullamcorper velit. Lectus magna fringilla urna porttitor rhoncus dolor purus non. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa. Felis donec et odio pellentesque. Turpis cursus in hac habitasse platea dictumst quisque sagittis purus. Faucibus purus in massa tempor nec feugiat nisl pretium fusce. Neque volutpat ac tincidunt vitae semper quis. Ut lectus arcu bibendum at varius."
    long_number = '12345678901234567890'
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
    cartURL = SauceDemoData.sauceURL+'cart.html'
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
    orderCheckoutSectionText = 'Checkout: Your Information'
    orderCheckoutFNameErrorMsg = 'Error: First Name is required'
    orderCheckoutLNameErrorMsg = 'Error: Last Name is required'
    orderCheckoutZipCodeErrorMsg = 'Error: Postal Code is required'
    
class SauceDemoOverview(object):
    orderOverviewURL = 'checkout-step-two.html'
class SauceDemoConfirmation(object):
    orderConfirmationURL = 'checkout-complete.html'
    
    successImageAlt = 'Pony Express'
    
    successMessage = 'Thank you for your order!'
    successCopy = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    