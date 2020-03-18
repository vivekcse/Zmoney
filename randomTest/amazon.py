from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Amazon(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Call Firefox browser
        cls.driver = webdriver.Chrome(executable_path=r'/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(30)
        # Load amazon.in site
        #cls.driver.get("https://www.amazon.in/")
        cls.driver.maximize_window()

    def test_amazon(self):
        self.driver.get("https://www.amazon.in/")
        # In the search box, enter ' data catalog' and search'
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iPhone XR (64GB) - Yellow")
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
        self.driver.implicitly_wait(5)

        iphone_title = "Apple iPhone XR (64GB) - Yellow"

        # check for title
        title = self.driver.find_element_by_xpath(
            '//*[contains(text(),"Apple iPhone XR (64GB) - Yellow")]').text.strip()
        self.assertEqual(iphone_title, title)

        # check for paperback price
        iphone_price = self.driver.find_element_by_css_selector('#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div > span > div > div > div:nth-child(2) > div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 > div > div:nth-child(2) > div.sg-col-4-of-24.sg-col-4-of-12.sg-col-4-of-36.sg-col-4-of-28.sg-col-4-of-16.sg-col.sg-col-4-of-20.sg-col-4-of-32 > div > div.a-section.a-spacing-none.a-spacing-top-small > div > div > a > span:nth-child(1) > span:nth-child(2) > span.a-price-whole').text.strip()
        #self.assertEqual(iphone_price, "48,900")

        print("Title = ", title)
        am = int(iphone_price.replace(',', ''))
        print("Iphone Price on Amazon is = ", iphone_price)

    @classmethod
    def tearDown(cls):
        # Close the browser
        cls.driver.quit()

    def test_iphone(self):
        self.driver.get('https://www.flipkart.com/')
        # In the search box, enter ' data catalog' and search'
        self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
        self.driver.find_element_by_xpath("//input[@type='text'] ").send_keys("iPhone XR (64GB) - Yellow")
        self.driver.find_element_by_xpath("//button[@type='submit']").submit()
        self.driver.implicitly_wait(500)

        iphone_title = "Apple iPhone XR (Yellow, 64 GB)"

        # check for title
        title = self.driver.find_element_by_xpath(
        '//*[contains(text(),"Apple iPhone XR (Yellow, 64 GB)")]').text.strip()
        #title.click()
        self.assertEqual(iphone_title, title)
        self.driver.find_element_by_xpath('//*[contains(text(),"Apple iPhone XR (Yellow, 64 GB)")]').click()

        # check for paperback price
        # Find parent handle -> Main Window
        parentHandle = self.driver.current_window_handle

        handles = self.driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                break
        self.driver.implicitly_wait(3)
        iphone_price1 = self.driver.find_element_by_css_selector(
        'div>div._3iZgFn>div._2i1QSc>div>div').text.strip()
        #self.assertEqual(iphone_price1, "₹49,900")

        print("Title = ", title)
        flip = int(iphone_price1[1:].replace(',', ''))
        print("Iphone Price on Flipkart = ", iphone_price1)

    @classmethod
    def tearDown(cls):
        # Close the browser
        cls.driver.quit()

    def test_pricecompare(self):
        print(am, flip)


if __name__ == "__main__":
    unittest.main()