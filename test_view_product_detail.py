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


    def test_case_TC17(self):
        search_bar = 'input[name="field-keywords"]'
        self.wait_for_element_visible(search_bar)
        self.type(search_bar, "laptop\n") 

        # 1. Wait for ANY product results to load
        product_selector = '//div[@data-component-type="s-search-result"]'
        self.wait_for_element_visible(product_selector, timeout=15)

        # 2. Use a "Relative" selector
        # This says: Find the first search result container, 
        # then find the first link inside an h2, no matter what the text is.
        target = '(//div[@data-component-type="s-search-result"]//h2/a | //div[@data-component-type="s-search-result"]//h2)[1]'

        # 3. Execution
        self.scroll_to_element(target)
        
        # Sometimes the h2 itself is clickable, sometimes it's the <a> inside.
        # self.click() in SeleniumBase is smart enough to handle this.
        self.click(target)

        # 4. Verification
        # The product detail page always has an ID "productTitle"
        self.wait_for_element_visible("#productTitle", timeout=15)
        print("Successfully navigated to product details.")