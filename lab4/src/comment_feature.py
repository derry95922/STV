import unittest
from keywords import *
from post_features import create_post, delete_post

class test_suite(unittest.TestCase):
    def setUp(self):
        print("")
        print('---setUp---')
        self.driver = login()
        create_post(self.driver)
    
    def tearDown(self):
        print("")
        print('---teardown---')
        delete_post(self.driver)
        logout(self.driver)

    def create_comment_on_admin_ui_page(self):
        print('---Create post on the Admin UI page---')

        wait_plus_icon_is_visible(self.driver, 'Posts', 'comments').click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        select_dropdown_by_field_name(self.driver, "author", "Demo User")
        select_dropdown_by_field_name(self.driver, "post", "CreatePost")

        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-ctpeu']")
        assert "Your changes have been saved successfully" in self.driver.find_element_by_xpath("//*[@class='css-ctpeu']").text
        actualID = self.driver.find_element(By.XPATH, "//*[@class='EditForm__name-field']").text
        wait_element_is_visible(self.driver, "//*[contains(@data-list-path,'comments')]").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        expectID = self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--id')]").text
        assert actualID == expectID

        delete_comment(self.driver)

    def edit_comment_on_admin_ui_page(self):
        print('---edit_comment_on_admin_ui_page---')
        create_comment(self.driver)

        wait_element_is_visible(self.driver, "//*[@class='octicon octicon-home']").click()
        wait_web_herf_is_visible(self.driver, "comments").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        originState = self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--select')]").text
        wait_element_is_visible(self.driver, "//*[contains(@class,'ItemList__value--id')]").click()
        select_dropdown_by_field_name(self.driver, "commentState", "Archived")
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()
        wait_element_is_visible(self.driver, "//*[contains(@data-list-path,'comments')]").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        actualState = self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--select')]").text
        assert "Archived" in actualState
        assert originState != actualState

        delete_comment(self.driver)

    def delete_comment_on_admin_ui_page(self):
        print('---delete_comment_on_admin_ui_page---')
        create_comment(self.driver)

        wait_element_is_visible(self.driver, "//*[@class='octicon octicon-home']").click()
        wait_web_herf_is_visible(self.driver, "comments").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(self.driver, "//*[contains(@class,'ItemList__value--id')]/../preceding-sibling::*").click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        wait_element_is_visible(self.driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(self.driver, "//*[text()='No comments found...']")
        noPosts = self.driver.find_element(By.XPATH, "//*[text()='No comments found...']").text
        assert "No comments found..." == noPosts

def create_comment(driver):
    wait_element_is_visible(driver, "//*[@class='octicon octicon-home']").click()
    wait_element_is_visible(driver, "//div[text()='Demo']")
    wait_plus_icon_is_visible(driver, 'Posts', 'comments').click()
    wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
    select_dropdown_by_field_name(driver, "author", "Demo User")
    select_dropdown_by_field_name(driver, "post", "CreatePost")

    wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
    wait_element_is_visible(driver, "//*[@class='css-2960tt']")
    wait_element_is_visible(driver, "//*[text()='Save']").click()
    wait_element_is_visible(driver, "//*[@class='css-ctpeu']")
    assert "Your changes have been saved successfully" in driver.find_element_by_xpath("//*[@class='css-ctpeu']").text
    actualID = driver.find_element(By.XPATH, "//*[@class='EditForm__name-field']").text
    wait_element_is_visible(driver, "//*[contains(@data-list-path,'comments')]").click()
    wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
    expectID = driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--id')]").text
    assert actualID == expectID

def delete_comment(driver):
    wait_element_is_visible(driver, "//*[contains(@data-list-path,'comments')]").click()
    wait_element_is_visible(driver, "//*[@class='ItemList__col']//*[text()='CreatePost']/../preceding-sibling::*").click()
    wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
    wait_element_is_visible(driver, "//*[text()='No comments found...']")
    noPosts = driver.find_element(By.XPATH, "//*[text()='No comments found...']").text
    assert "No comments found..." == noPosts

def suite():
    suite = unittest.TestSuite()

    suite.addTests([test_suite('create_comment_on_admin_ui_page'),
                    test_suite('edit_comment_on_admin_ui_page'),
                    test_suite('delete_comment_on_admin_ui_page'),
                    ])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())