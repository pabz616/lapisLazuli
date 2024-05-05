from demoQAComponentLocators.pageElements import ListLocators
from playwright.sync_api import expect


class ListPage:
    def __init__(self, page):
        self.page = page
        self.pageHeader = page.locator(ListLocators.PAGE_HEADER)
        self.list = page.locator(ListLocators.LIST)
        self.row1 = page.locator(ListLocators.ROW1)
        self.row2 = page.locator(ListLocators.ROW2)
        self.row3 = page.locator(ListLocators.ROW3)
        self.row4 = page.locator(ListLocators.ROW4)
        self.row5 = page.locator(ListLocators.ROW5)
        self.row6 = page.locator(ListLocators.ROW6)
        
        
    def checkUI(self):
        pageHeaderCopy = 'Sortable'

        expect(self.pageHeader).to_be_visible()
        expect(self.pageHeader).to_contain_text(pageHeaderCopy)
        #
        expect(self.list).to_be_visible()
        #
        expect(self.row1).to_be_visible()
        expect(self.row1).to_contain_text('One')
        
        expect(self.row2).to_be_visible()
        expect(self.row2).to_contain_text('One')
        
        expect(self.row3).to_be_visible()
        expect(self.row3).to_contain_text('Three')
        
        expect(self.row4).to_be_visible()
        expect(self.row4).to_contain_text('Four')
        
        expect(self.row5).to_be_visible()
        expect(self.row5).to_contain_text('Five')
        
        expect(self.row6).to_be_visible()
        expect(self.row6).to_contain_text('Six')
        
    def sort_list(self):
        """Drag row element to new position"""
        self.row1.drag_to(self.row2)
        self.row3.drag_to(self.row6)
        self.row5.drag_to(self.row4)
        
    def confirm_list_was_sorted(self):
        expect(self.row1).to_contain_text('Two')
        expect(self.row2).to_contain_text('One')
        expect(self.row3).to_contain_text('Five')
        expect(self.row4).to_contain_text('Four')
        expect(self.row5).to_contain_text('Six')
        expect(self.row6).to_contain_text('Three')