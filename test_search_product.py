from seleniumbase import BaseCase

class TestSearchProduct(BaseCase):
    """These test cases test whether the website returns any results if users
       type valid, invalid, special keyword, and verify if the website automatically 
       recommend other searching keyword to users"""

    def setUp(self):
        super().setUp()
        print()
        print("---- RUNNING BEFORE THE TEST ----")
        self.open("https://www.amazon.com/") 
        self.maximize_window()
        
        self.wait_for_element_present("body")
        
        if self.is_element_visible('button[alt="Continue shopping"]'):
            self.click('button[alt="Continue shopping"]')
        
        self.sleep(5) 

    def tearDown(self):        
        self.clear_local_storage()
        self.clear_session_storage()
        self.delete_all_cookies()
        super().tearDown()
        print("---- END OF TEST ----")

    def test_case_TC01(self):
        """The test verifies if the website returns the result of products when searching valid search keyword"""
        search_bar = 'input[name="field-keywords"]'
        
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) 
        
        self.send_keys(search_bar, "laptop") 
        self.sleep(2)
        
        self.click("#nav-search-submit-button") 
        
        self.wait_for_element_visible('div[data-component-type="s-search-result"]', timeout=15)
        # wait for the product list to appear
        self.assert_element('div[data-component-type="s-search-result"]')
        # verify if the product list appears
        self.save_screenshot("TC01_screenshot.png", "Test Case Screenshots")

    def test_case_TC02(self):
        """The test verifies if the website returns the result of products when searching invalid keyword"""
        search_bar = 'input[name="field-keywords"]'
        
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) 
        
        self.send_keys(search_bar, "wfhhr2h3iuh32ih23iuwdhfi") 
        self.sleep(2)
        
        self.click("#nav-search-submit-button") 
        
        self.wait_for_text("No results for", "span", timeout=15)
        
        self.save_screenshot("TC02_screenshot.png", "Test Case Screenshots")

    def test_case_TC03(self):
        """The test verifies if the website returns the result of products when searching keyword with special characters"""
        search_bar = 'input[name="field-keywords"]'
        
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) 
        
        self.send_keys(search_bar, "@!#$") 
        self.sleep(2)
        
        self.click("#nav-search-submit-button") 
        
        self.wait_for_text("No results for", "span", timeout=15)
        self.save_screenshot("TC03_screenshot.png", "Test Case Screenshots")

    def test_case_TC04(self):
        """The test verifies the search suggestion flyout appears when typing"""
        search_bar = 'input[name="field-keywords"]'
        
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) 
        
        self.send_keys(search_bar, "laptop") 
        
        self.wait_for_element_visible(".left-pane-results-container", timeout=10)
        self.assert_element_visible(".left-pane-results-container")
        
        self.save_screenshot("TC04_screenshot.png", "Test Case Screenshots")