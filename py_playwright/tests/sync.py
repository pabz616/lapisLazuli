from playwright.sync_api import sync_playwright
from locators.pageElements import QuotesPageLocators

def main():
    with sync_playwright() as spw:
        #TEST DATA
        quotes_url = 'http://quotes.toscrape.com/'
        email_address = 'foo@example.com'
        pwd = 'password123'
        
        #TEST
        browser = spw.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto(quotes_url)
        page.query_selector(QuotesPageLocators.LOGIN_LINK).is_visible()  
        page.query_selector(QuotesPageLocators.LOGIN_LINK).click()
        
        #VISUAL CHECKS
        page.query_selector(QuotesPageLocators.USN_INPUT).is_visible()
        page.query_selector(QuotesPageLocators.USN_INPUT).is_editable()
        
        page.query_selector(QuotesPageLocators.PWD_INPUT).is_visible()
        page.query_selector(QuotesPageLocators.PWD_INPUT).is_editable()
        
        page.query_selector(QuotesPageLocators.SUBMIT_BTN).is_visible()
        page.query_selector(QuotesPageLocators.SUBMIT_BTN).is_enabled()
        
        
        #ACTION EVENT
        page.query_selector(QuotesPageLocators.USN_INPUT).type(email_address)
        page.query_selector(QuotesPageLocators.PWD_INPUT).type(pwd)
        page.query_selector(QuotesPageLocators.SUBMIT_BTN).click()

        #CHECK LOGIN IS SUCCESSFUL
        try:
            page.wait_for_selector(QuotesPageLocators.LOGOUT_LINK, timeout=5000)
        except:
            print('Login was unsuccessful')
            exit()
            
        #GET ALL THE QUOTES
        quotes = page.query_selector_all(QuotesPageLocators.QUOTES_TEXT)
        
        for quote in quotes:
            quote.query_selector('.text').is_visible()
            print(quote.query_selector('.text').inner_text())
            
        browser.close()
        
if __name__ == '__main__':
    main()