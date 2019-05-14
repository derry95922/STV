import unittest
from keywords import *

class test_suite(unittest.TestCase):
    def create_a_new_user_on_admin_ui_page(self):
        driver = login()
        
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@data-section-label='Users']//*[contains(@data-list-path,'users')]//a[@title='Create']")).perform()
        wait_plus_icon_is_visible(driver, "Users", "users").click()

        wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
        input_text(driver, "//*[@name='name.first']", "firstName")
        input_text(driver, "//*[@name='name.last']", "lastName")
        mail_name = datetime.now().strftime('%Y%m%d%H%M%S')+"@gmail.com"
        input_text(driver, "//*[@name='email']", mail_name)
        input_text(driver, "//*[@name='password']", "ilove5278")
        input_text(driver, "//*[@name='password_confirm']", "ilove5278")
        wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(driver, "//*[@class='css-nil']")
        input_text(driver, "//*[@name='phone']", "0987654321")
        wait_element_is_visible(driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(driver, "//*[text()='Save']").click()
        wait_element_is_visible(driver, "//*[contains(@data-list-path,'users')]").click()
        wait_element_is_visible(driver, "//a[text()='Users']").click()
        options = driver.find_elements(By.XPATH, "//*[contains(@class,'ItemList__value--email')]")
        # for option in options:
        #     print(option.text)
        assert mail_name in [option.text for option in options]

        logout(driver)

def suite():
    suite = unittest.TestSuite()

    suite.addTests([test_suite('create_a_new_user_on_admin_ui_page')])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())