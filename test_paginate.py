from seleniumbase import BaseCase

class TestPaginate(BaseCase):
    def setUp(self):
        """These test cases test whether the user can switch to the next page
        or previous page to see products by clicking to a page number or the arrow"""

    def setUp(self):
        # Open the Amazon website at the maximum window size and wait
        # for the website to be stable
        super().setUp()
        print()
        print("---- RUNNING BEFORE THE TEST ----")
        self.open("https://www.amazon.com/") 
        self.maximize_window()
        
       # Wait for the body to ensure page load
        self.wait_for_element_present("body")
        
        self.click_if_visible('button[alt="Continue shopping"]') 
        # click "Continue Shopping" to continue, avoiding the program to terminate suddenly
        self.sleep(5) 

    def tearDown(self):        
        # Clear all cookies so the next test starts with a fresh login screen
        self.clear_local_storage()
        self.clear_session_storage()
        self.delete_all_cookies()
        super().tearDown()
        print("---- END OF TEST ----")

    def test_case_TC13(self):
        """This test verifies if the user can switch to the next page by clicking the
        page number"""

        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "Bag\n") # type keyword and press Enter

        self.wait_for_element_present("body")
        
        pagination_bar = 'div[role="navigation"][aria-label="pagination"]'
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.sleep(3)
        self.save_screenshot("TC13_screenshot(1).png", "Test Case Screenshots")

        self.click('a[aria-label="Go to page 3"]') # click to switch to page 3
        
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.hover('body') # hover to the body for a clear screenshot
        self.sleep(3)

        self.save_screenshot("TC13_screenshot(2).png", "Test Case Screenshots")

    def test_case_TC14(self):
        """This test verifies if the user can switch to the previous page by clicking the
        page number"""
        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "Bag\n") # type keyword and press Enter

        self.wait_for_element_present("body")
        
        pagination_bar = 'div[role="navigation"][aria-label="pagination"]'
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.sleep(3)

        self.click('a[aria-label="Go to page 3"]') # click to switch to page 3
        
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.hover('body')
        self.sleep(3)
        self.save_screenshot("TC14_screenshot(1).png", "Test Case Screenshots")

        self.click('a[aria-label="Go to page 1"]') # click to switch to page 1

        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.hover('body')
        self.sleep(3)

        self.save_screenshot("TC14_screenshot(2).png", "Test Case Screenshots")

    def test_case_TC15(self):
        """This test verifies if the user can switch to the next page by clicking 
        the arrow"""

        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "Bag\n") # type keyword and press Enter

        self.wait_for_element_present("body")

        pagination_bar = 'div[role="navigation"][aria-label="pagination"]'
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.sleep(3)
        self.save_screenshot("TC15_screenshot(1).png", "Test Case Screenshots")

        self.click('a[aria-label*="next page"]')
                
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.hover('body')
        self.sleep(3)
        self.save_screenshot("TC15_screenshot(2).png", "Test Case Screenshots")

    def test_case_TC16(self):
        """This test verifies if the user can switch to the previous page by clicking 
        the arrow"""

        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "Bag\n") # type keyword and press Enter

        self.wait_for_element_present("body")

        pagination_bar = 'div[role="navigation"][aria-label="pagination"]'
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.sleep(3)

        self.click('a[aria-label*="next page"]')
                
        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.hover('body')
        self.sleep(3)
        self.save_screenshot("TC16_screenshot(1).png", "Test Case Screenshots")

        self.click('a[aria-label*="previous page"]')

        self.wait_for_element_visible(pagination_bar)
        self.scroll_to_element(pagination_bar)
        self.hover('body')
        self.sleep(3)
        self.save_screenshot("TC16_screenshot(2).png", "Test Case Screenshots")







