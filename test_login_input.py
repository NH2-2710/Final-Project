from seleniumbase import BaseCase

class LoginTest(BaseCase):

    def setUp(self): 
    # to run the program before every test begins
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

    def tearDown(self):
        # Clear all cookies so the next test starts with a fresh login screen
        self.clear_local_storage()
        self.clear_session_storage()
        self.delete_all_cookies()
        super().tearDown()

    def test_case_TC01(self):
        """TC01: Verify the login procedure is executed correctly
        and allow when the user to log in if they enter the correct 
        telephone and password"""
        self.wait_for_element_visible('input[name="tel"]')
        # wait for the text field "Số điện thoại" to be visible
        self.click('input[name="tel"]')
        # click the text field "Số điện thoại" if visible
        # and verify whether the user can click the text field before typing information

        self.send_keys('input[name="tel"]', "0337998047")
        # send the telephone number which exists in the system to the text field
        self.save_screenshot("filled_telephone.png", "TC01_screenshots")
        # save the screenshot after filling the telephone number text field
        self.click_if_visible('button:contains("Tiếp Tục")')
        # click "Tiếp Tục" button
        self.wait_for_element_visible('input[type="password"]')

        self.send_keys('input[type="password"]', "Huyhoang@2710")
        # send the correct password associated to the telephone number
        self.save_screenshot("filled_password.png", "TC01_screenshots")
        # save the screenshot after filling the telephone number text field

        self.click('button:contains("Đăng Nhập")')
        # click the "Đăng Nhập" button to log in
        self.save_screenshot("login_successfully.png", "TC01_screenshots")
        # save the screenshot after logging in successfully
        self.click_if_visible("img[alt='close-icon']")
        # click the close button in the ad window appears logging in if the ad appears

        self.hover_on_element("[data-view-id='header_header_account_container']")
        # hover the mouse on the Tài khoản button
        self.save_screenshot("sub-options in Tài khoản.png", "TC01_Screenshots")
        # save the screenshot showing sub options in Tài khoản button
        self.wait_for_element_visible('p:contains("Thông tin tài khoản")')
        # hover to the "Tài khoản" section to make more options in this section appears
        self.assert_elements("div[data-view-id='header_header_account_container'] p")
        # to verify if options in "Tài khoản" section including "Thông tin tài khoản",
        # "Hạng TikiVIP của bạn", "Đơn hàng của tôi", "Trung tâm hỗ trợ", "Đăng xuất" are present

        print("The test case TC01 has been tested successfully")
        # This statement will be printed if the compiler can reach to the end of the program
        # else, the compiler is stuck somewhere in the progra indicating an error pops up

    def test_case_TC02(self):
        """This test verifies whether the system allow the user to enter a number that
        is more than 10 digits"""
        invalid_number = "03373412325" # assign a number with 11 digits to the variable
        self.send_keys('input[name="tel"]', invalid_number) # input the 11-digits number to the text field
        self.save_screenshot("filled_telephone.png", "TC02_screenshots")
        try: 
            self.assert_text(invalid_number[0:len(invalid_number)], 'input[name="tel"]')
            # verify whether the invalid number is typed completely in the text field
            # or any extra number is excluded
        except Exception:
            print("The system doesn't allow user to enter more than 10 digits in the field")
            # print the statement if there is an error
        print("The test case TC02 has been tested successfully")
            # print the statement indicating that the test has been completed successfully

    def test_case_TC03(self):
        """This test verifies whether the system allows the user to enter a number that
        is less than 10 digits"""
        invalid_number = "033799804" # assign a number with 9 digits to the variable
        self.send_keys('input[name="tel"]', invalid_number)
        # type the invalid number to the text field
        self.save_screenshot("filled_telephone.png", "TC03_screenshots")
        # save the screenshot of filling invalid number to the text field
        self.click('button:contains("Tiếp Tục")')
        self.sleep(3)
        self.assert_text("Số điện thoại không đúng định dạng.", ".error-mess")
        # verify if the system notifies the error to the user showing that the number is not correctly formatted
        self.save_screenshot("error_notified.png", "TC03_screenshots")
        # save the screenshot notifying the phone number is not formatted correctly
        print("The test case TC03 has been tested successfully")

    def test_case_TC04(self):
        """This test verifies whether the system notifies the 
        user that their number is not formatted correctly 
        when they try to log in with a number in which the 
        first number is not 0"""
        invalid_number = "3371231122" # assign a number that does not start with 0
        self.send_keys('input[name=tel]', invalid_number)
        # type the invalid number to the text field
        self.save_screenshot("filled_telephone.png", "TC04_screenshots")
        # save the screenshot of filling invalid number to the text field
        self.click('button:contains("Tiếp Tục")')
        self.sleep(3)
        self.assert_text("Số điện thoại không đúng định dạng", ".error-mess")
        # verify if the system notifies the error to the user
        # showing that the number is not correctly formatted
        self.save_screenshot("error_notified.png", "TC04_screenshots")
        print("The test case TC04 has been tested successfully")

    def test_case_TC05(self):
        """The test verifies if the system tells the user
        to not leave the field blank when they try to do that"""
        self.save_screenshot("blank_telphone.png", "TC05_screenshots")
        self.click('button:contains("Tiếp Tục")')
        self.sleep(3)
        self.assert_text("Số điện thoại không được để trống", ".error-mess")
        # verify if the system notifies the error to the user and
        # tell them not to leave the field blank
        self.save_screenshot("error_notified.png", "TC05_screenshots")
        print("The test case TC05 has been tested successfully")

    def test_case_TC06(self):
        """The test verifies whether the system begins procedure
        to create a new account for user if the telephone is 
        formatted correctly but is not registered in the system"""

        unregistered_number = "0378921316"
        self.send_keys('input[name=tel]', unregistered_number)
        # enter the number in the telephone number field
        self.save_screenshot("filled_telephone.png", "TC06_screenshots")
        self.sleep(3) # stop the program temporarily for 3 seconds
        self.click('button:contains("Tiếp Tục")') # click the "Tiếp Tục" button
        self.sleep(3) # stop the program temporarily for 3 seconds
        self.assert_text("Nhập mã xác minh", 'h4:contains("Nhập mã xác minh")')
        # check if the correct text appears 
        self.save_screenshot("begin_authentication.png", "TC06_screenshots")
        # save the screenshot of the test
        print("The test case TC06 has been tested successfully")

    def test_case_TC07(self):
        """The test verifies whether the system prevents the 
        user to log in if they enter the wrong password"""

        registered_number = "0337998047"
        wrong_password = "ererewr"
        self.send_keys('input[name=tel]', registered_number)
        # enter the number in the telephone number field
        self.save_screenshot("filled_telephone.png", "TC07_screenshots")
        self.click('button:contains("Tiếp Tục")')
        self.sleep(3)
        self.send_keys('input[type="password"]', wrong_password)
        # enter the password in the password field
        self.click('button:contains("Đăng Nhập")')
        self.assert_text("Thông tin đăng nhập không đúng", ".error-mess")
        self.save_screenshot("error_notified.png", "TC07_screenshots")
        print("The test case TC07 has been tested successfully")

    def test_case_TC08(self):
        """The test verifies whether the system prevents the user log
        in if they leave the password field blank"""

        registered_number = "0337998047"
        self.send_keys('input[name=tel]', registered_number)
        self.save_screenshot("filled_telephone.png", "TC08_screenshots")
        self.click('button:contains("Tiếp Tục")')
        self.sleep(3)
        self.click('button:contains("Đăng Nhập")')
        self.assert_text("Mật khẩu không được để trống", ".error-mess")
        self.save_screenshot("error_notified.png", "TC08_screenshots")

        print("The test case TC08 has been tested successfully")




        