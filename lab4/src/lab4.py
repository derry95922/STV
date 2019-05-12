import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def wait_element_is_visible(driver, locate, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locate)))
    except Exception:
        driver.quit()
    finally:
        return element

def wait_plus_icon_is_visible(driver, title, subtitle, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-section-label='%s']//*[contains(@data-list-path,'%s')]//a[@title='Create']" % (title, subtitle))))
    except Exception:
        driver.quit()
    finally:
        return element

def wait_web_herf_is_visible(driver, subtitle, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@data-list-path,'%s')]//*[@class='dashboard-group__list-label']" % (subtitle))))
    except Exception:
        driver.quit()
    finally:
        return element

def input_text(driver, locate, text):
    try:
        wait_element_is_visible(driver, locate)
        driver.find_element_by_xpath(locate).send_keys(text)
    except Exception:
        driver.quit()    

def select_dropdown_by_field_name(driver, field_name, target, timeout=10):
    try:
        wait_element_is_visible(driver, "//*[@for='%s']//*[@class='Select-multi-value-wrapper']" % (field_name)).click()
        wait_element_is_visible(driver, "//*[@for='%s']//*[text()='%s']" % (field_name, target)).click()
    except Exception:
        driver.quit()

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
    driver.quit()

def create_post(driver):
    wait_plus_icon_is_visible(driver, 'Posts', 'posts').click()
    wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
    input_text(driver, "//*[@name='name']", "CreatePost")
    wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
    wait_element_is_visible(driver, "//*[@data-list-path='posts']").click()
    wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
    assert "CreatePost" in driver.find_element_by_xpath("//*[text()='CreatePost']").text

class test_suite(unittest.TestCase):
    def setUp(self):
        print("")
        print('---setUp---')
        self.driver = login()

    def create_post_on_the_admin_ui_page(self):
        print('---Create post on the Admin UI page---')
        wait_plus_icon_is_visible(self.driver, 'Posts', 'posts').click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        input_text(self.driver, "//*[@name='name']", "CreatePost")
        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-ctpeu']")
        assert "Your changes have been saved successfully" in self.driver.find_element_by_xpath("//*[@class='css-ctpeu']").text
        wait_element_is_visible(self.driver, "//*[@data-list-path='posts']").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "CreatePost" in self.driver.find_element_by_xpath("//*[text()='CreatePost']").text

    def edit_post_on_the_admin_ui_page(self):
        print('---edit_post_on_the_admin_ui_page---')
        wait_web_herf_is_visible(self.driver, "posts").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "Demo User" not in self.driver.find_element_by_xpath("//*[@class='ItemList__col' and not(child::*)]").text
        wait_element_is_visible(self.driver, "//*[text()='CreatePost']").click()
        select_dropdown_by_field_name(self.driver, "author", "Demo User")
        wait_element_is_visible(self.driver, "//*[text()='Save']").click()
        wait_element_is_visible(self.driver, "//*[@data-list-path='posts']").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "Demo User" in self.driver.find_element_by_xpath("//*[contains(@class, 'ItemList__value--relationship')]").text
        
    def search_posts_by_keyword_on_the_admin_ui_page(self):
        print('---search_posts_by_keyword_on_the_admin_ui_page---')
        wait_web_herf_is_visible(self.driver, "posts").click()
        input_text(self.driver, "//*[@class='css-foh633']", "CreatePost")
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        expectResult = self.driver.find_element(By.XPATH, "//*[@class='css-foh633']").get_attribute("value")
        actualResult = self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text
        assert expectResult in actualResult
        wait_element_is_visible(self.driver, "//*[@class='css-1h0bkr6']").click()
        input_text(self.driver, "//*[@class='css-foh633']", "expectNoResult")
        expectNoResult = self.driver.find_element(By.XPATH, "//*[@class='css-foh633']").get_attribute("value")
        assert expectNoResult not in actualResult
        wait_element_is_visible(self.driver, "//*[@class='css-l1jroy']")

    def delete_post_on_the_admin_ui_page(self):
        print('---delete_post_on_the_admin_ui_page---')
        wait_web_herf_is_visible(self.driver, "posts").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(self.driver, "//*[@class='ItemList__col']//*[text()='CreatePost']/../preceding-sibling::*").click()
        wait_element_is_visible(self.driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(self.driver, "//*[text()='No posts found...']")
        noPosts = self.driver.find_element(By.XPATH, "//*[text()='No posts found...']").text
        assert "No posts found..." == noPosts

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

    def edit_comment_on_admin_ui_page(self):
        print('---edit_comment_on_admin_ui_page---')
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

    def delete_comment_on_admin_ui_page(self):
        print('---delete_comment_on_admin_ui_page---')
        wait_web_herf_is_visible(self.driver, "comments").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(self.driver, "//*[contains(@class,'ItemList__value--id')]/../preceding-sibling::*").click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        wait_element_is_visible(self.driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(self.driver, "//*[text()='No comments found...']")
        noPosts = self.driver.find_element(By.XPATH, "//*[text()='No comments found...']").text
        assert "No comments found..." == noPosts

    def create_category_on_admin_ui_page(self):
        print('---create_category_on_admin_ui_page---')
        wait_plus_icon_is_visible(self.driver, 'Posts', 'categories').click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        input_text(self.driver, "//*[@name='name']", "CreateCategory")
        wait_element_is_visible(self.driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(self.driver, "//*[contains(@data-list-path,'categories')]").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        assert "CreateCategory" in self.driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text

    def show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page(self):
        print('---show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page---')
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

        wait_element_is_visible(self.driver, "//*[@class='octicon octicon-sign-out']").click()
        wait_element_is_visible(self.driver, "//*[@class='auth-box__brand']").click()
        wait_element_is_visible(self.driver, "//li//*[text()='Blog']").click()
        wait_element_is_visible(self.driver, "//*[@class='badge pull-right']").click()

        actualResult = self.driver.find_element(By.XPATH, "//*[@class='media-heading']").text
        assert actualResult == expectResult

        admin = {'account':'demo@keystonejs.com','password':'demo'}
        wait_element_is_visible(self.driver, "//*[text()='Sign In']").click()
        input_text(self.driver, "//*[@name='email']",admin['account'])
        input_text(self.driver, "//*[@name='password']",admin['password'])
        wait_element_is_visible(self.driver, "//*[text()='Sign In']").click()
        wait_element_is_visible(self.driver, "//div[text()='Demo']")
        wait_web_herf_is_visible(self.driver, "posts").click()
        wait_element_is_visible(self.driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(self.driver, "//*[@class='ItemList__col']//*[text()='CreatePost']/../preceding-sibling::*").click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        wait_element_is_visible(self.driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-l1jroy']")
        wait_element_is_visible(self.driver, "//*[contains(@data-list-path,'categories')]").click()
        wait_element_is_visible(self.driver, "//*[@class='css-1xkojxp']")
        wait_element_is_visible(self.driver, "//*[@class='octicon octicon-trashcan']").click()
        wait_element_is_visible(self.driver, "//*[@data-screen-id='modal-dialog']")
        wait_element_is_visible(self.driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(self.driver, "//*[@class='css-l1jroy']")

    def tearDown(self):
        print('---teardown---')
        logout(self.driver)

def suite():
    suite = unittest.TestSuite()

    '''
    suite.addTests([test_suite('create_post_on_the_admin_ui_page'),
                    test_suite('edit_post_on_the_admin_ui_page'),
                    test_suite('search_posts_by_keyword_on_the_admin_ui_page'),
                    test_suite('create_comment_on_admin_ui_page'),
                    test_suite('edit_comment_on_admin_ui_page'),
                    test_suite('delete_comment_on_admin_ui_page'),
                    test_suite('delete_post_on_the_admin_ui_page'),
                    test_suite('create_category_on_admin_ui_page'),
                    test_suite('show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page')])
    '''

    suite.addTests([test_suite('create_post_on_the_admin_ui_page'),
                    test_suite('edit_post_on_the_admin_ui_page'),
                    test_suite('search_posts_by_keyword_on_the_admin_ui_page'),
                    test_suite('create_comment_on_admin_ui_page'),
                    test_suite('edit_comment_on_admin_ui_page'),
                    test_suite('delete_comment_on_admin_ui_page'),
                    test_suite('delete_post_on_the_admin_ui_page'),
                    test_suite('create_category_on_admin_ui_page'),
                    test_suite('show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page')])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())