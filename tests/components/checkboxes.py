import asyncio
from playwright.async_api import async_playwright, expect

async def checkbox():
    async with async_playwright() as apw:
        demoQAURL = "https://demoqa.com"
        home_chxbox = 'label[for="tree-node-home"]'
        msg = "You have selected :homedesktopnotescommandsdocuments"
        #CREATE NEW CONTEXT
        browser = await apw.chromium.launch(headless=False)
        context = await browser.new_context()
        
        #FOR DEBUGGING
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        
        #INTERACT WITH CHECKBOX
        await page.goto(demoQAURL+'/checkbox')
        await page.check(home_chxbox)
        await page.screenshot(path="screenshots/checkbox.png")
        await page.is_checked(home_chxbox) is True
        await expect(page.locator("#result")).to_contain_text(msg)
        await context.tracing.stop(path="logs/trace.zip")
           
        #CLOSE BROWSER
        await browser.close()
        
asyncio.run(checkbox())
        