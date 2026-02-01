from seleniumbase import BaseCase

class TestSearchFilter(BaseCase):
    """These test cases verify whether the website return the result of products, which is
       satisfied the criteria mentioned in the filters."""

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

    def test_case_TC09(self):
        """This test case tests a scenario in which a user is searching
        for unisex clothes, with the cost in range of $50 - $100, the color is black,
        the size is M, clothing material is cotton, occasion is Birthday"""

        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "clothes\n") # type keyword and press Enter
        
        # 1. Filter by Unisex
        unisex_filter = 'a[aria-label="Apply Unisex filter to narrow results"]'
        self.wait_for_element_visible(unisex_filter)
        self.scroll_to_element(unisex_filter)
        self.sleep(3)
        self.click(unisex_filter)
        self.sleep(3) # click "Unisex" category
        
        # 2. Filter by Black Color
        # Note: We wait for the page to refresh after the first filter
        black_filter = 'a[aria-label="Apply Black filter to narrow results"]'
        self.wait_for_element_visible(black_filter)
        self.scroll_to_element(black_filter)
        self.sleep(3)
        self.click(black_filter)
        self.sleep(3) # click "Black" color filter
        
        # 3. Filter by Size M
        size_m_button = 'button[value="M"]'
        self.wait_for_element_visible(size_m_button)
        self.scroll_to_element(size_m_button)
        self.sleep(3)
        self.click(size_m_button)
        self.sleep(3) # choose the M size
        
        self.save_screenshot("TC09_screenshot.png", "Test Case Screenshots")

    def test_case_TC10(self):
        """This test case verifies that a user can clear all applied filters"""
        # (This is a great 10th use case!)
        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.click(search_bar) # click on the search engine
        self.send_keys(search_bar, "clothes\n") # type keyword and press Enter

        # Apply one filter
        self.click('a[aria-label="Apply Unisex filter to narrow results"]')
        self.save_screenshot("TC10_screenshot(1).png", "Test Case Screenshots")
        
        # Click "Clear" to reset
        clear_link = 'a:contains("Clear")'
        if self.is_element_visible(clear_link):
            self.click(clear_link)
            self.assert_element_not_visible(clear_link)

        self.sleep(3)
        self.save_screenshot("TC10_screenshot(2).png", "Test Case Screenshots")