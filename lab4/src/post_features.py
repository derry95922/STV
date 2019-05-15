import unittest
from keywords import *

class test_suite(unittest.TestCase):
    def setUp(self):
        # print("")
        # print('---setUp---')
        self.driver = login()
    
    def tearDown(self):
        # print("")
        # print('---teardown---')
        logout(self.driver)
    
    def create_post_on_the_admin_ui_page(self):
        # print('---Create post on the Admin UI page---')
  
        wait_plus_icon_is_visible(self.driver, 'Posts', 'posts').click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        input_text(self.driver, "//*[@name='name']", "CreatePost")
        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()
        wait_element_is_visible(self.driver, "//*[@data-list-path='posts']").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "CreatePost" in self.driver.find_element_by_xpath("//*[text()='CreatePost']").text
        
        delete_post(self.driver)

    def edit_post_on_the_admin_ui_page(self):
        # print('---edit_post_on_the_admin_ui_page---')
        create_post(self.driver)

        wait_web_herf_is_visible(self.driver, "posts").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "Demo User" not in self.driver.find_element_by_xpath("//*[@class='ItemList__col' and not(child::*)]").text
        wait_element_is_visible(self.driver, "//*[text()='CreatePost']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-1wrt3l9 field-type-relationship']")
        select_dropdown_by_field_name(self.driver, "author", "Demo User")
        
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[text()='Relationships']")).perform()
        wait_element_is_visible(self.driver, "//*[@class='css-2960tt']").click() #save_btn
        wait_element_is_visible(self.driver, "//*[@class='active']//*[text()='Posts']").click()
        
        assert "Demo User" in self.driver.find_element_by_xpath("//*[contains(@class, 'ItemList__value--relationship')]").text
        
        delete_post(self.driver)

    def search_posts_by_keyword_on_the_admin_ui_page(self):
        # print('---search_posts_by_keyword_on_the_admin_ui_page---')
        create_post(self.driver)

        wait_web_herf_is_visible(self.driver, "posts").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        input_text(self.driver, "//*[@class='css-foh633']", "CreatePost")
        expectResult = self.driver.find_element(By.XPATH, "//*[@class='css-foh633']").get_attribute("value")
        actualResult = self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text
        assert expectResult in actualResult
        wait_element_is_visible(self.driver, "//*[@class='css-1h0bkr6']").click()    #X_btn
        input_text(self.driver, "//*[@class='css-foh633']", "expectNoResult")
        expectNoResult = self.driver.find_element(By.XPATH, "//*[@class='css-foh633']").get_attribute("value")
        assert expectNoResult not in actualResult
        wait_element_is_visible(self.driver, "//*[@class='css-l1jroy']")
        wait_element_is_visible(self.driver, "//*[@class='active']//*[text()='Posts']").click()

        delete_post(self.driver)

    def delete_post_on_the_admin_ui_page(self):
        # print('---delete_post_on_the_admin_ui_page---')
        create_post(self.driver)

        wait_web_herf_is_visible(self.driver, "posts").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(self.driver, "//*[@class='ItemList__col']//*[text()='CreatePost']/../preceding-sibling::*").click()
        wait_element_is_visible(self.driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(self.driver, "//*[text()='No posts found...']")
        noPosts = self.driver.find_element(By.XPATH, "//*[text()='No posts found...']").text
        assert "No posts found..." == noPosts

def create_post(driver):
    wait_plus_icon_is_visible(driver, 'Posts', 'posts').click()
    wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
    input_text(driver, "//*[@name='name']", "CreatePost")
    wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
    wait_element_is_visible(driver, "//*[@class='css-2960tt']")
    wait_element_is_visible(driver, "//*[text()='Save']").click()
    wait_element_is_visible(driver, "//*[@data-list-path='posts']").click()
    wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
    assert "CreatePost" in driver.find_element_by_xpath("//*[text()='CreatePost']").text
    wait_element_is_visible(driver, "//*[@class='octicon octicon-home']").click()
    wait_element_is_visible(driver, "//div[text()='Demo']")

def delete_post(driver):
    wait_element_is_visible(driver, "//*[contains(@data-list-path,'posts')]").click()
    wait_element_is_visible(driver, "//*[@class='ItemList__col']//*[text()='CreatePost']/../preceding-sibling::*").click()
    wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
    wait_element_is_visible(driver, "//*[text()='No posts found...']")
    noPosts = driver.find_element(By.XPATH, "//*[text()='No posts found...']").text
    assert "No posts found..." == noPosts

def suite():
    suite = unittest.TestSuite()

    suite.addTests([test_suite('create_post_on_the_admin_ui_page'),
                    test_suite('edit_post_on_the_admin_ui_page'),
                    test_suite('search_posts_by_keyword_on_the_admin_ui_page'),
                    test_suite('delete_post_on_the_admin_ui_page'),
                    ])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())