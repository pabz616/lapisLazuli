from components.demoQAComponentLocators.pageElements import CheckBoxLocators
from playwright.sync_api import expect


class CheckBoxPage:
    def __init__(self, page):
        self.page = page
        self.pageHeader = page.locator(CheckBoxLocators.PAGE_HEADER)

        self.homeDirectoryToggle = page.locator(CheckBoxLocators.HOME_TOGGLE)
        self.desktopDirectoryToggle = page.locator(CheckBoxLocators.DESKTOP_TOGGLE)
        
        self.homeCheckboxLabel = page.locator(CheckBoxLocators.HOME_CHKBX_TITLE)
        self.expandButton = page.locator(CheckBoxLocators.EXPAND)
        self.collapseButton = page.locator(CheckBoxLocators.COLLAPSE)
        self.messageElement = page.locator(CheckBoxLocators.MESSAGE)
        
        self.home_directory = page.locator(CheckBoxLocators.SUBDIR1)
        self.sd1 = page.locator(CheckBoxLocators.SUBDIR2)
        self.sd2 = page.locator(CheckBoxLocators.SUBDIR3)
        self.sd3 = page.locator(CheckBoxLocators.SUBDIR4)
        self.sd4 = page.locator(CheckBoxLocators.SUBDIR5)
        self.sd5 = page.locator(CheckBoxLocators.SUBDIR6)
        self.sd6 = page.locator(CheckBoxLocators.SUBDIR7)
        self.sd7 = page.locator(CheckBoxLocators.SUBDIR8)
        self.sd8 = page.locator(CheckBoxLocators.SUBDIR9)
        
    def checkUI(self):
        pageHeaderCopy = 'Check Box'
        homeCheckboxLabelCopy = 'Home'
       
        expect(self.pageHeader).to_be_visible()
        expect(self.pageHeader).to_contain_text(pageHeaderCopy)
        #
        expect(self.homeCheckbox).to_be_visible()
        expect(self.homeCheckbox).not_to_be_checked()
        expect(self.homeCheckboxLabel).to_be_visible()
        expect(self.homeCheckboxLabel).to_contain_text(homeCheckboxLabelCopy)
        #
        expect(self.expandButton).to_be_visible()
        expect(self.expandButton).to_be_enabled()
        #
        expect(self.collapseButton).to_be_visible()
        expect(self.collapseButton).to_be_enabled()
    
    def displayMessage(self):
        self.homeCheckbox.click()
        expect(self.messageElement).to_be_visible()
        
    def hideMessage(self):
        self.homeCheckbox.click()
        expect(self.messageElement).to_be_visible()
        
        self.homeCheckbox.click()
        expect(self.messageElement).not_to_be_visible()
        
    def expandHomeDirectory(self):
        self.homeDirectoryToggle.click()
        
    def expandDesktopDirectory(self):
        self.desktopDirectoryToggle.click()

    def confirmDisplayOfHomeSubDirectories(self):
        desktop_directory = self.sd1
        documents_directory = self.sd2
        downloads_directory = self.sd3
        
        expect(self.home_directory).to_be_visible()
        expect(self.home_directory).to_contain_text('Home')
        #
        expect(desktop_directory).to_be_visible()
        expect(desktop_directory).to_contain_text('Desktop')
        #
        expect(documents_directory).to_be_visible()
        expect(documents_directory).to_contain_text('Documents')
        #
        expect(downloads_directory).to_be_visible()
        expect(downloads_directory).to_contain_text('Downloads')
        
    def confirmDisplayOfDesktopSubdirectories(self):
        desktop_notes = self.sd2
        desktop_commands = self.sd3
        
        expect(desktop_notes).to_be_visible()
        expect(desktop_notes).to_contain_text('Notes')
        #
        expect(desktop_commands).to_be_visible()
        expect(desktop_commands).to_contain_text('Commands')
     
    def expandAllDirectories(self):
        self.expandButton.click()

    def confirmDisplayOfAllSubDirectories(self):
        expect(self.home_directory).to_be_visible()
        expect(self.sd1).to_be_visible()
        expect(self.sd2).to_be_visible()
        expect(self.sd3).to_be_visible()
        expect(self.sd4).to_be_visible()
        expect(self.sd5).to_be_visible()
        expect(self.sd6).to_be_visible()
        expect(self.sd7).to_be_visible()
        expect(self.sd8).to_be_visible()
       
    def collapseAllDirectories(self):
        self.collapseButton.click()
    
    def confirmSubDirectoriesAreHidden(self):
        desktop_directory = self.sd1
        documents_directory = self.sd2
        downloads_directory = self.sd3
        
        expect(self.home_directory).not_to_be_visible()
        expect(desktop_directory).not_to_be_visible()
        expect(documents_directory).not_to_be_visible()
        expect(downloads_directory).not_to_be_visible()