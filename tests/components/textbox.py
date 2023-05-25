import asyncio
from playwright.async_api import async_playwright, expect

async def textbox():
    async with async_playwright() as apw:
        demoQAURL = "https://demoqa.com"
        demoQAName = "hortence"
        demoQAEmail = "awesomeQA@mail.com"
        demoQAAddress = "123 Main Street - Apt. 3, New York, NY  10010"
        
        #CREATE NEW CONTEXT
        browser = await apw.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        #FORM ELEMENTS
        name = page.locator('[id="userName"]')
        email = page.locator('[id="userEmail"]')
        current_address = page.locator('[id="currentAddress"]')
        perm_address = page.locator('[id="permanentAddress"]')
        submitBtn = page.locator('[id="submit"]')
        result = page.locator('[id="output"]')
        
        #INTERACT WITH INPUTS
        await page.goto(demoQAURL+'/text-box')
        await name.fill(demoQAName)
        await email.fill(demoQAEmail)
        await current_address.fill(demoQAAddress)
        await perm_address.fill(demoQAAddress)
        await submitBtn.click()
        await expect(result).not_to_be_empty()
        await expect(result).to_contain_text("Name:" + demoQAName)
        
        #CLOSE BROWSER
        await browser.close()
        
asyncio.run(textbox())
        