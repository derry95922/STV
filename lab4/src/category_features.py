import unittest
from keywords import *
from post_features import delete_post

class test_suite(unittest.TestCase):
    def setUp(self):
        # print("")
        # print('---setUp---')
        self.driver = login()
    
    def tearDown(self):
        # print("")
        # print('---teardown---')
        logout(self.driver)
    
    def create_category_on_admin_ui_page(self):
        # print('---create_category_on_admin_ui_page---')

        wait_plus_icon_is_visible(self.driver, 'Posts', 'categories').click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        input_text(self.driver, "//*[@name='name']", "CreateCategory")
        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[contains(@data-list-path,'categories')]").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "CreateCategory" in self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text

        delete_category(self.driver)

    def show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page(self):
        # print('---show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page---')
        create_category(self.driver)
        logout(self.driver)
        self.driver = login()

        wait_element_is_visible(self.driver, "//*[@class='octicon octicon-home']").click()   #createData
        wait_plus_icon_is_visible(self.driver, 'Posts', 'posts').click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        input_text(self.driver, "//*[@name='name']", "CreatePost")
        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-1r0jf0q item-name-field']")
        expectResult = self.driver.find_element(By.XPATH, "//*[@class='css-1r0jf0q item-name-field']").get_attribute("value")
        select_dropdown_by_field_name(self.driver, "state", "Published")
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@class='Relationships']")).perform()
        select_dropdown_by_field_name(self.driver, "categories", "CreateCategory")
        wait_element_is_visible(self.driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()

        wait_element_is_visible(self.driver, "//*[@class='octicon octicon-sign-out']").click()   #logout
        wait_element_is_visible(self.driver, "//*[@class='auth-box__brand']").click()
        wait_element_is_visible(self.driver, "//li//*[text()='Blog']").click()
        wait_element_is_visible(self.driver, "//*[@class='badge pull-right']").click()

        actualResult = self.driver.find_element(By.XPATH, "//*[@class='media-heading']").text
        assert actualResult == expectResult

        self.driver.quit()
        self.driver = login()
        wait_web_herf_is_visible(self.driver, "posts").click()
        delete_post(self.driver)
        delete_category(self.driver)

def create_category(driver):
    wait_plus_icon_is_visible(driver, 'Posts', 'categories').click()
    wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
    input_text(driver, "//*[@name='name']", "CreateCategory")
    wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
    wait_element_is_visible(driver, "//*[contains(@data-list-path,'categories')]").click()
    wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
    assert "CreateCategory" in driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text

def delete_category(driver):
    wait_element_is_visible(driver, "//*[contains(@data-list-path,'categories')]").click()
    wait_element_is_visible(driver, "//*[@class='css-1xkojxp']")
    wait_element_is_visible(driver, "//*[@class='octicon octicon-trashcan']").click()
    wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
    wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
    wait_element_is_visible(driver, "//*[@class='css-l1jroy']")

def suite():
    suite = unittest.TestSuite()

    suite.addTests([test_suite('create_category_on_admin_ui_page'),
                    test_suite('show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page'),
                    ])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())