import unittest

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# driver = webdriver.Chrome()
# driver.get("http://127.0.0.1:3000/")

def wait_element_is_visible(driver, locate, timeout=5):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locate)))
    except Exception:
        driver.close()
    finally:
        return element

def wait_plus_icon_is_visible(driver, title, subtitle, timeout=5):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-section-label='%s']//*[@data-list-path='%s']//a[@title='Create']" % (title, subtitle))))
    except Exception:
        driver.close()
    finally:
        return element

def input_text(driver, locate, text):
    try:
        driver.find_element_by_xpath(locate).send_keys(text)
    except Exception:
        driver.close()    

def login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:3000/")

    admin = {'account':'demo@keystonejs.com','password':'demo'}
    driver.maximize_window()
    wait_element_is_visible(driver, "//*[text()='Sign in']").click()
    input_text(driver, "//*[@name='email']",admin['account'])
    input_text(driver, "//*[@name='password']",admin['password'])
    wait_element_is_visible(driver, "//*[text()='Sign In']").click()
    wait_element_is_visible(driver, "//div[text()='Demo']")

    return driver

def logout(driver):
    wait_element_is_visible(driver, "//*[@class='octicon octicon-sign-out']").click()
    driver.close()

class test_suite(unittest.TestCase):
    def setUp(self):
        print("")
        print('---setUp---')
        self.driver = login()

    def create_post_on_the_admin_ui_page(self):
        print('---Create post on the Admin UI page---')
        # sleep(1)
        wait_plus_icon_is_visible(self.driver, 'Posts', 'posts').click()
        # sleep(1)
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        input_text(self.driver, "//*[@name='name']", "CreatePost")
        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()
        sleep(1)
        assert "Your changes have been saved successfully" in self.driver.find_element_by_xpath("//*[@class='css-ctpeu']").text
        wait_element_is_visible(self.driver, "//*[@data-list-path='posts']").click()
        sleep(1)
        assert "CreatePost" in self.driver.find_element_by_xpath("//*[text()='CreatePost']").text

    def test_divide(self):
        print('---测试用例test_simple divide---')

    def tearDown(self):
        print('---teardown---')
        logout(self.driver)

def suite():
    suite = unittest.TestSuite()
    suite.addTests([test_suite('create_post_on_the_admin_ui_page')])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())