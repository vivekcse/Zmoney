from selenium import webdriver
from time import sleep
import unittest


class Facebook(unittest.TestCase):
    usr = input('Enter Email Id:')
    pwd = input('Enter Password:')
    @classmethod
    def setUp(cls):
        # Call Firefox browser
        cls.driver = webdriver.Chrome(executable_path=r'C:\\Users\\vivek.yadav\\PycharmProjects\\weInvest\\drivers\\chromedriver.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_facebook(self):
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.facebook.com/')
        self.driver.maximize_window()
        assert "Facebook" in self.driver.title
        sleep(1)

        username_box = self.driver.find_element_by_id('email')
        username_box.send_keys(self.usr)
        print("Email Id entered")
        sleep(1)

        password_box = self.driver.find_element_by_id('pass')
        password_box.send_keys(self.pwd)
        print("Password entered")

        login_box = self.driver.find_element_by_id('loginbutton')
        login_box.click()
        sleep(3)
        print("Login Succesfull")

        elem = self.driver.find_element_by_css_selector(".input.textInput")
        elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
        elem = self.driver.find_element_by_css_selector(".selected")
        elem.click()
        sleep(5)


    @classmethod
    def tearDown(cls):
        # Close the browser
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()