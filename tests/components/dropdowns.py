import asyncio
from playwright.async_api import async_playwright, expect

async def dropdown_menus():
    async with async_playwright() as apw:
        demoQAURL = "https://demoqa.com/select-menu"
       
        #CREATE NEW CONTEXT
        browser = await apw.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        #FORM ELEMENTS
        ddl_with_groups = page.locator('[id="withOptGroup"]')
        ddl_single = page.locator('[id="selectOne"]')
        ddl_v1 = page.locator('[id="oldSelectMenu"]')
        ddl_multi = page.locator('[id="#"]')
        ddl_multi_v1 = page.locator('[id="cars"]')
        
        #SELECT VALUE GROUPED
        await page.goto(demoQAURL)
        await ddl_with_groups.click()
        await ddl_with_groups.press('ArrowDown+Enter')
        await expect(ddl_with_groups).to_contain_text('Group 1, option 2')
        
        #SELECT VALUE SINGLE
        await ddl_single.click()
        await page.get_by_text("Prof.").click()
        await expect(ddl_single).to_contain_text('Prof.')
        
        #SELECT FROM OLD-SCHOOL MENU
        await ddl_v1.click()
        await ddl_v1.select_option('Blue')
        await expect(ddl_v1).to_contain_text('Blue')
        
        #SELECT OPTION
        await page.select_option('select#cars', ['volvo', 'saab', 'audi'])
        await expect(ddl_multi_v1).not_to_contain_text('honda')
        
        #CLOSE BROWSER
        await browser.close()
        
asyncio.run(dropdown_menus())
        