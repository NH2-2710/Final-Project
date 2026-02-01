from seleniumbase import BaseCase

class TestBrowseCategory(BaseCase):
    """These test cases verify whether users can search products by browsing to 
        various categories and can scroll up and down"""
    
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
        self.sleep(10) 
        

    def tearDown(self):        
        # Clear all cookies so the next test starts with a fresh login screen
        self.clear_local_storage()
        self.clear_session_storage()
        self.delete_all_cookies()
        super().tearDown()
        print("---- END OF TEST ----")

    def test_case_TC05(self):
        """The test verifies if users can open and see the list of different categories
           and scroll down to see these categories"""

        self.click("#nav-hamburger-menu")
        self.sleep(2)
        category_list_selector = '#hmenu-content'
        scroll_selector = 'div.hmenu-visible[data-menu-id="1"]'
        self.assert_element_visible(category_list_selector)
        if self.is_element_visible(category_list_selector):
            print("The menu of category list is displayed")
        else:
            self.fail("The menu of category list should be visible but it is hidden")
        total_height = int(self.get_property(scroll_selector, "scrollHeight"))
        # get the height of the scrollable menu
        
        if total_height == 0: 
            total_height = 2000
        # prevent the menu scroll won't happen in test case

        self.save_screenshot("TC05_screenshot(1).png", "Test Case Screenshots")

        # test scroll down the menu
        for position in range(0, total_height, 100):
            self.execute_script(f"document.querySelector('{scroll_selector}').scrollTop = {position};")
            self.sleep(0.1)

        self.save_screenshot("TC05_screenshot(2).png", "Test Case Screenshots")

        # test scroll up the menu
        for position in range(total_height, -100, -100):
            self.execute_script(f"document.querySelector('{scroll_selector}').scrollTop = {position};")
            self.sleep(0.1)
        
        self.save_screenshot("TC05_screenshot(3).png", "Test Case Screenshots")

    def test_case_TC06(self):
        """The test verifies if users can search products by 
        navigating to Electronics --> Wearable Technology category,"""
        self.click("#nav-hamburger-menu")
        self.wait_for_element_visible('#hmenu-content')
        self.assert_element_visible('#hmenu-content')
        
        electronics_item = 'a.hmenu-item[data-menu-id="6"]'
        self.scroll_to_element(electronics_item)
        self.sleep(1)
        self.click(electronics_item)
        
        self.save_screenshot("TC06_screenshot(1).png", "Test Case Screenshots")
        
        wearable_link = 'a[href*="wearable_technology"]'
        self.wait_for_element_visible(wearable_link) # Ensuring sub-menu loaded
        self.scroll_to_element(wearable_link)
        self.sleep(1)
        self.click(wearable_link)
        
        self.save_screenshot("TC06_screenshot(2).png", "Test Case Screenshots")
        
        # verify header contains the category name
        self.assert_text("Wearable Technology")
        self.save_screenshot("TC06_screenshot(3).png", "Test Case Screenshots")

    def test_case_TC07(self):
        """The test verifies if users can search products by 
        navigating to See All --> Home and Kitchen --> Kids' Home Store category,"""
        self.click("#nav-hamburger-menu")
        self.wait_for_element_visible('#hmenu-content')
        self.assert_element_visible('#hmenu-content')
        
        see_all_btn = 'a[aria-label="See all"]'
        self.scroll_to_element(see_all_btn)
        self.click(see_all_btn)
        
        self.save_screenshot("TC07_screenshot(1).png", "Test Case Screenshots")
        
        home_kitchen_item = 'a[data-menu-id="18"]'
        self.wait_for_element_visible(home_kitchen_item)
        self.scroll_to_element(home_kitchen_item)
        self.click(home_kitchen_item)
        
        self.save_screenshot("TC07_screenshot(2).png", "Test Case Screenshots")
        
        kids_home_link = 'a[href*="kids_home_store"]'
        self.wait_for_element_visible(kids_home_link)
        self.scroll_to_element(kids_home_link)
        self.click(kids_home_link)
        
        # Verification of final destination
        self.wait_for_element_visible("h1")
        self.save_screenshot("TC07_screenshot(3).png", "Test Case Screenshots")

    def test_case_TC08(self):
        """The test verifies if users can go back to the main menu 
        after browsing to sub categories"""

        self.click("#nav-hamburger-menu")
        self.wait_for_element_visible('#hmenu-content')
        self.assert_element_visible('#hmenu-content')
        
        self.scroll_to_element('a[aria-label="See all"]')
        self.click('a[aria-label="See all"]')
        
        self.save_screenshot("TC08_screenshot(1).png", "Test Case Screenshots")
        
        # Navigate into a sub-menu
        self.wait_for_element_visible('a[data-menu-id="18"]')
        self.click('a[data-menu-id="18"]')
        
        self.save_screenshot("TC08_screenshot(2).png", "Test Case Screenshots")
        
        # Click Back
        back_btn = 'a[aria-label="Back to main menu"]'
        self.wait_for_element_visible(back_btn)
        self.click(back_btn)
        
        # Resetting scroll to 0 to ensure content is visible in screenshot
        self.execute_script("document.querySelector('div.hmenu-visible').scrollTop = 0;")
        
        self.assert_element_visible('#hmenu-content')
        self.sleep(2) # Short wait for slide animation to complete
        self.save_screenshot("TC08_screenshot(3).png", "Test Case Screenshots")