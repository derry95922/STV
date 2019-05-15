import unittest
from keywords import *

class test_suite(unittest.TestCase):
    def create_enquiry_on_the_contact_page(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:3000/")
        driver.maximize_window()
        wait_element_is_visible(driver, "//li//*[text()='Contact']").click()

        input_text(driver, "//*[@name='name.full']", "testName")
        input_text(driver, "//*[@name='email']", "demo@keystonejs.com")
        input_text(driver, "//*[@name='phone']", "0987654321")
        wait_element_is_visible(driver, "//*[@name='enquiryType']").click()
        wait_element_is_visible(driver, "//*[text()='Just leaving a message']").click()
        input_text(driver, "//*[@name='message']", "testMessage")
        actualName = driver.find_element(By.XPATH, "//*[@name='name.full']").get_attribute("value")
        wait_element_is_visible(driver, "//*[text()='Submit']").click()
        wait_element_is_visible(driver, "//*[text()='Success!']")
        assert "Success" in driver.find_element(By.XPATH, "//*[text()='Success!']").text

        driver.quit()
        driver = login()

        wait_element_is_visible(driver, "//a[text()='Enquiries']").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        expectName = driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--name')]").text
        assert actualName == expectName

        delete_enquiry(driver)
        logout(driver)

    def delete_enquiry_on_admin_ui_page(self):
        create_enquiry()
        driver = login()

        wait_element_is_visible(driver, "//a[text()='Enquiries']").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(driver, "//*[contains(@class,'ItemList__value--name')]/../preceding-sibling::*").click()
        wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
        wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(driver, "//*[text()='No enquiries found...']")
        noEnquiries = driver.find_element(By.XPATH, "//*[text()='No enquiries found...']").text
        assert "No enquiries found..." == noEnquiries

        logout(driver)

def create_enquiry():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:3000/")
    driver.maximize_window()
    wait_element_is_visible(driver, "//li//*[text()='Contact']").click()

    input_text(driver, "//*[@name='name.full']", "testName")
    input_text(driver, "//*[@name='email']", "demo@keystonejs.com")
    input_text(driver, "//*[@name='phone']", "0987654321")
    wait_element_is_visible(driver, "//*[@name='enquiryType']").click()
    wait_element_is_visible(driver, "//*[text()='Just leaving a message']").click()
    input_text(driver, "//*[@name='message']", "testMessage")
    wait_element_is_visible(driver, "//*[text()='Submit']").click()
    wait_element_is_visible(driver, "//*[text()='Success!']")
    assert "Success" in driver.find_element(By.XPATH, "//*[text()='Success!']").text

    driver.quit()

def delete_enquiry(driver):
    wait_element_is_visible(driver, "//a[text()='Enquiries']").click()
    wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
    wait_element_is_visible(driver, "//*[contains(@class,'ItemList__value--name')]/../preceding-sibling::*").click()
    wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
    wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
    wait_element_is_visible(driver, "//*[text()='No enquiries found...']")
    noEnquiries = driver.find_element(By.XPATH, "//*[text()='No enquiries found...']").text
    assert "No enquiries found..." == noEnquiries

def suite():
    suite = unittest.TestSuite()

    suite.addTests([test_suite('create_enquiry_on_the_contact_page'),
                    test_suite('delete_enquiry_on_admin_ui_page'),
                    ])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())