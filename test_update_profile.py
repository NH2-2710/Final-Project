from seleniumbase import BaseCase

class UpdateProfileTest(BaseCase):
    def setUp(self):
        super().setUp()
        """This procedures opens the windows of "TIKI" website and close ad windows and open
        login window to prepare inputting information for logging"""
        print("RUNNING BEFORE THE TEST")

        self.open("https://tiki.vn/") # open the website "TIKI"
        self.maximize_window() # make the window open at maximum size
        self.sleep(5)
        self.wait_for_element_visible(".tiki-logo", timeout = 3)
        # verify if the TIKI's logo appears on the webpage
        self.click_if_visible("img[alt='close-icon']", timeout = 3) 
        # click the close button of the first advertisement window appears on the webpage

        self.sleep(5)

        self.click_if_visible("[data-view-id='header_header_account_container']", timeout = 3)
        # click the "Tài khoản" if it is visible on the webpage
        self.assert_element('button:contains("Tiếp Tục")')
        # to verify if the "Tiếp tục" button is available on the Login window
        self.assert_element('button:contains("Tiếp Tục")')
        self.send_keys('input[name="tel"]', "0337998047") 
        self.click_if_visible('button:contains("Tiếp Tục")')
        self.send_keys('input[type="password"]', "Huyhoang@2710")
        self.click('button:contains("Đăng Nhập")')
        self.click_if_visible("img[alt='close-icon']", timeout = 5) 

    def tearDown(self):
        # Clear all cookies so the next test starts with a fresh login screen
        self.clear_local_storage()
        self.clear_session_storage()
        self.delete_all_cookies()
        super().tearDown() 

    def test_case_TC09():
        self.hover_on_element("[data-view-id='header_header_account_container']")
        self.hover_on_element('p[title="Thông tin tài khoản"]')
        self.click('p[title="Thông tin tài khoản"]')


