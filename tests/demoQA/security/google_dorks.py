"""
RECON STEP: USING GOOGLE DORKS
src: https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/
src: https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06
"""

import webbrowser

google = "https://www.google.com"


def run_search(dork):
    webbrowser.open(google+f"/search?q={dork}")

# ###*******************************************#######


def search_site(url):
    """The “site” operator allows you to search within a specific website or domain."""
    run_search("site:"+url+" "+"steganography")

    
def search_cache(url):
    """The query cache: will show the version of the web page that Google has in its cache."""
    run_search("cache:"+url)


def search_intext(url):
    """The “intext” operator searches for web pages with specific words on the page"""
    run_search("intext:”index of” password")
    
    
def search_allintext(url):
    """The “allintext” operator searches for web pages with entire words on the page"""
    run_search("allintext:”index of” password")
    
    
def search_intitle(url):
    """The “intitle” operator searches for web pages with specific words or phrases in the title tag"""  
    run_search("intitle:”index of” password")
    
    
def search_inurl(url):
    """The “inurl” operator searches for web pages that contain specific words or phrases in the URL."""
    run_search("inurl:admin.php")
    

def search_for_link(url):
    """The “link” operator searches for web pages that link to a specific URL."""
    run_search("link:"+url+"/admin")
    

def search_for_related(url):
    """List web pages that are “similar” to a specified web page."""
    run_search("related:"+url)

    
def search_for_filetype(url):
    """Use the “filetype” operator to search for specific file types"""
    run_search("filetype:pdf"+" "+"site:"+url)

# ###*******************************************###### #


url = input("Please enter the url you want to search: ")
search_site(url)
search_cache(url)
search_intext(url)
search_allintext(url)
search_intitle(url)
search_inurl(url)
search_for_link(url)
search_for_related(url)
# search_for_filetype(url)