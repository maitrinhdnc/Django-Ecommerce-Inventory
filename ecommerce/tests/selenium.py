# Setup code 
import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# fixture: function attacth to test before the test run
# scope: share fixture accross classes (function, package, session)
@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.add_argument("--headless=new")
    # options.headless = False 
    """
    When run selenium test, browser appear on the sreen
    and we can see the test being run, if we just do it in the background, 
    set headless is false
    """
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()