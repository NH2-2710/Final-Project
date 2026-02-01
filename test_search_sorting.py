from seleniumbase import BaseCase

class TestSearchSorting(BaseCase):
    def setUp(self):
        """These test cases test whether the website sort the result in a specific order.
        For example: from low to high price, from high to low price"""

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

    def test_case_TC11(self):
        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "Bag\n") # type keyword and press Enter

        sorting_selector = 'span[data-action="a-dropdown-button"]'
        self.wait_for_element_visible(sorting_selector)
        self.wait_for_element_present("body")

        self.click(sorting_selector)
        self.wait_for_element_visible('a[data-value*="price-asc-rank"]')
        self.click('a[data-value*="price-asc-rank"]') # click to sort price from Low to High

        self.wait_for_element_present("body")
        self.save_screenshot("TC11_screenshot(1).png", "Test Case Screenshots")
        self.sleep(5)
        
        # Scroll down the page slowly
        for x in range(0, 2200, 100):
            self.execute_script(f"window.scrollTo(0, {x});")
            self.sleep(0.1)

        self.save_screenshot("TC11_screenshot(2).png", "Test Case Screenshots")
        self.sleep(5)

    def test_case_TC12(self):
        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "Bag\n") # type keyword and press Enter

        sorting_selector = 'span[data-action="a-dropdown-button"]'
        self.wait_for_element_visible(sorting_selector)
        self.wait_for_element_present("body")

        self.click(sorting_selector)
        self.wait_for_element_visible('a[data-value*="price-desc-rank"]')
        self.click('a[data-value*="price-desc-rank"]') # click to sort price from Low to High

        self.wait_for_element_present("body")
        self.save_screenshot("TC12_screenshot(1).png", "Test Case Screenshots")
        self.sleep(5)
        
        # Scroll down the page slowly
        for x in range(0, 2200, 100):
            self.execute_script(f"window.scrollTo(0, {x});")
            self.sleep(0.1)

        self.save_screenshot("TC12_screenshot(2).png", "Test Case Screenshots")
        self.sleep(5)        



          