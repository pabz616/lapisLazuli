import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd, DemoQA
from e2e.demoQAPages.demoQABookStoreSearch import BookStoreSearchPage as Search

from faker import Faker
fake = Faker()


@pytest.mark.high
class TestHighBookStoreSearch:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        bookStoreUrl = DemoQA.baseUrl+'/books'
        page.goto(bookStoreUrl)
        yield

    def test_BookStore_valid_search_is_successful(self, page: Page):
        """Test bookstore search feature - valid book"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm('JavaScript')
        onBookStoreSearch.confirmResults


@pytest.mark.normal
class TestNormalBookStoreSearch:
    def test_BookStore_valid_search_no_results(self, page: Page):
        """Test bookstore search feature - valid term, no results"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm('Python')
        onBookStoreSearch.confirmNoResults
        
    def test_BookStore_invalid_search(self, page: Page):
        """Test bookstore search feature - invalid term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(fake.word())
        onBookStoreSearch.confirmNoResults
        
    def test_BookStore_boundary_search(self, page: Page):
        """Test bookstore search feature - large amount of text as term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(fake.text(max_nb_chars=255))
        onBookStoreSearch.confirmNoResults
    
    def test_BookStore_alphaNumeric_search(self, page: Page):
        """Test bookstore search feature - mixed alpha-numeric term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(fake.uuid4())
        onBookStoreSearch.confirmNoResults
    
    def test_BookStore_mixedCharSet_search(self, page: Page):
        """Test bookstore search feature - mixed characters (cyrillic, chinese, etc.) term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.mixedCharSet)
        onBookStoreSearch.confirmNoResults
        
    def test_BookStore_foreign_search(self, page: Page):
        """Test bookstore search feature - arabic characters term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.sanskrit)
        onBookStoreSearch.confirmNoResults
     
    @pytest.mark.security  
    def test_BookStore_formatExploit_SQL_Injection(self, page: Page):
        """Test bookstore search feature - format exploit: SQL injection term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.sqlInjection)
        onBookStoreSearch.confirmNoResults
     
    @pytest.mark.security   
    def test_BookStore_formatExploit_JS_Injection(self, page: Page):
        """Test bookstore search feature - format exploit: SQL injection term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.jsInjection)
        onBookStoreSearch.confirmNoResults
    
    @pytest.mark.security
    def test_BookStore_formatExploit_BrokenHTML(self, page: Page):
        """Test bookstore search feature - format exploit: Broken HTML term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.brokenHTML)
        onBookStoreSearch.confirmNoResults
    
    @pytest.mark.security
    def test_BookStore_formatExploit_XSS_ImageTag(self, page: Page):
        """Test bookstore search feature - Cross-site scripting with image tag, using alert() term"""
        
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.xssImageTag)
        onBookStoreSearch.confirmNoResults