import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from demoQAUtils.data import DemoQA
from demoQAUtils.book_selection import BookSelection
from demoQAUtils.injection_parameters import InjectionParameters as IP
file_path = '../../demoQA/demoQAUtils/payload.txt'


# PAYLOAD FILE
with open(file_path) as file:
    payload = file.read()

# INJECTION PARAMETERS
injection_params = IP.select_injection_parameters()      

ISBN = BookSelection.select_a_book()
DemoQA = DemoQA.baseUrl
redirect_url = "https://www.hackthissite.org/"

PAGES = {
    f"{DemoQA}/Books",
    f"{DemoQA}/Books?book={ISBN}",
    f"{DemoQA}/login",
    f"{DemoQA}/register",
    f"{DemoQA}/profile"
}


@pytest.mark.security
@pytest.mark.parametrize("target_url", PAGES)
class TestForcedURLRedirect:
    def test_url_redirect_with_domain_parameters(self, page: Page, target_url):
        forced_redirect_url = target_url+f"{injection_params}"+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(redirect_url), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_with_payload(self, page: Page, target_url):        
        forced_redirect_url = target_url+"&url="+payload
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(payload), f"Vulnerability found! Forced redirected to {payload} was successful"
        
    def test_url_redirect_with_whitelisted_word(self, page: Page, target_url):
        forced_redirection = target_url+"?image_url="+redirect_url
        page.goto(forced_redirection)
        expect(page).not_to_have_url(f"{redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_with_subdomain_same_as_target(self, page: Page, target_url):
        forced_redirect_url = target_url+"."+target_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(forced_redirect_url), f"Vulnerability found! Forced redirected to {forced_redirect_url} was successful"
        
    def test_url_redirect_with_redirection_by_XSS(self, page: Page, target_url):
        """Using CRLF to bypass "javascript" blacklisted keyword"""
        redirect_url = "java%0d%0ascript%0d%0a:alert(0)"
        forced_redirect_url = target_url+"?destination="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_double_backslash_to_bypass_HTTP_blacklisted_keyword(self, page: Page, target_url):
        redirect_url = "//google.com"
        forced_redirect_url = target_url+"?destination="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_triple_backslash_to_bypass_HTTP_blacklisted_keyword(self, page: Page, target_url):
        redirect_url = "///google.com"
        forced_redirect_url = target_url+"?destination="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_HTTPS_to_bypass_double_forward_slash(self, page: Page, target_url):
        redirect_url = "https:google.com"
        forced_redirect_url = target_url+"?destination="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
            
    def test_url_redirect_using_escape_sequence_to_bypass_double_forward_slash(self, page: Page, target_url):
        redirect_url = "\/\/google.com/"
        forced_redirect_url = target_url+"?destination="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_url_encoding_to_bypass_blacklisted_period_character(self, page: Page, target_url):
        redirect_url = "//google%E3%80%82com"
        forced_redirect_url = target_url+"?redir="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
            
    def test_url_redirect_using_null_byte_to_bypass_blacklist_filter(self, page: Page, target_url):
        redirect_url = "//google%00.com"
        forced_redirect_url = target_url+"?redir="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"https:{redirect_url}"), f"Vulnerability found! Forced redirected to https:{redirect_url} was successful"
        
    def test_url_redirect_using_parameter_pollution(self, page: Page, target_url):
        redirect_url = "?next=whitelisted.com&next=google.com"
        forced_redirect_url = target_url+"?redir="+redirect_url
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"{redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_using_at_character(self, page: Page, target_url):
        """browser will redirect to anything after the "@" """
        
        forced_redirect_url = redirect_url+"@demoqa.com"
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"{DemoQA}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
        
    def test_url_redirect_creating_folder_as_their_domain(self, page: Page, target_url):    
        forced_redirect_url = f"{target_url}/{redirect_url}"
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"{redirect_url}"), f"Vulnerability found! Forced redirected to {redirect_url} was successful"
    
    @pytest.mark.xfail(reason="page fails to load, but url loads with redirect parameter")    
    def test_url_redirect_using_xss_from_data_wrapper(self, page: Page, target_url):
        forced_redirect_url = f"{target_url}/redirect.php?url=data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ+Cg=="
        page.goto(forced_redirect_url)
        expect(page).not_to_have_url(f"{forced_redirect_url}"), f"Vulnerability found! Forced redirected to {forced_redirect_url} was successful"

