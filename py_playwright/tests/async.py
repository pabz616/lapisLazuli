import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        #for browser_type in [p.chromium, p.firefox, p.webkit]
        #await page.screenshot(path=f'example-{browser_type.name}.png')
        
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto('http://whatsmyuseragent.org/')
        print(await page.title())
        await browser.close()

asyncio.run(main())