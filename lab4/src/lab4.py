import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

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

def create_enquiry():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:3000/")
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

class test_suite(unittest.TestCase):
    # def setUp(self):
        # print("")
        # print('---setUp---')
        # self.driver = login()
    
    # def tearDown(self):
        # print("")
        # print('---teardown---')
        # logout(self.driver)

    def create_post_on_the_admin_ui_page(self):
        print('---Create post on the Admin UI page---')
        driver = login()
  
        wait_plus_icon_is_visible(driver, 'Posts', 'posts').click()
        wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
        input_text(driver, "//*[@name='name']", "CreatePost")
        wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(driver, "//*[text()='Save']").click()
        wait_element_is_visible(driver, "//*[@data-list-path='posts']").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        assert "CreatePost" in driver.find_element_by_xpath("//*[text()='CreatePost']").text
        
        delete_post(driver)
        logout(driver)

    def edit_post_on_the_admin_ui_page(self):
        print('---edit_post_on_the_admin_ui_page---')
        driver = login()
        create_post(driver)

        wait_web_herf_is_visible(driver, "posts").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        assert "Demo User" not in driver.find_element_by_xpath("//*[@class='ItemList__col' and not(child::*)]").text
        wait_element_is_visible(driver, "//*[text()='CreatePost']").click()
        wait_element_is_visible(driver, "//*[@class='css-1wrt3l9 field-type-relationship']")
        select_dropdown_by_field_name(driver, "author", "Demo User")
        # sleep(3)
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[text()='Relationships']")).perform()
        wait_element_is_visible(driver, "//*[@class='css-2960tt']").click() #save_btn
        # sleep(1)
        wait_element_is_visible(driver, "//*[@class='active']//*[text()='Posts']").click()
        # sleep(3)
        assert "Demo User" in driver.find_element_by_xpath("//*[contains(@class, 'ItemList__value--relationship')]").text
        
        delete_post(driver)
        logout(driver)

    def search_posts_by_keyword_on_the_admin_ui_page(self):
        print('---search_posts_by_keyword_on_the_admin_ui_page---')
        driver = login()
        create_post(driver)

        wait_web_herf_is_visible(driver, "posts").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        input_text(driver, "//*[@class='css-foh633']", "CreatePost")
        expectResult = driver.find_element(By.XPATH, "//*[@class='css-foh633']").get_attribute("value")
        actualResult = driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text
        assert expectResult in actualResult
        wait_element_is_visible(driver, "//*[@class='css-1h0bkr6']").click()    #X_btn
        input_text(driver, "//*[@class='css-foh633']", "expectNoResult")
        expectNoResult = driver.find_element(By.XPATH, "//*[@class='css-foh633']").get_attribute("value")
        assert expectNoResult not in actualResult
        wait_element_is_visible(driver, "//*[@class='css-l1jroy']")
        wait_element_is_visible(driver, "//*[@class='active']//*[text()='Posts']").click()

        delete_post(driver)
        logout(driver)

    def delete_post_on_the_admin_ui_page(self):
        print('---delete_post_on_the_admin_ui_page---')
        driver = login()
        create_post(driver)

        wait_web_herf_is_visible(driver, "posts").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(driver, "//*[@class='ItemList__col']//*[text()='CreatePost']/../preceding-sibling::*").click()
        wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(driver, "//*[text()='No posts found...']")
        noPosts = driver.find_element(By.XPATH, "//*[text()='No posts found...']").text
        assert "No posts found..." == noPosts

        logout(driver)

    def create_comment_on_admin_ui_page(self):
        print('---Create post on the Admin UI page---')
        driver = login()
        create_post(driver)

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

        delete_comment(driver)
        delete_post(driver)
        logout(driver)

    def edit_comment_on_admin_ui_page(self):
        print('---edit_comment_on_admin_ui_page---')
        driver = login()
        create_post(driver)
        create_comment(driver)

        wait_element_is_visible(driver, "//*[@class='octicon octicon-home']").click()
        wait_web_herf_is_visible(driver, "comments").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        originState = driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--select')]").text
        wait_element_is_visible(driver, "//*[contains(@class,'ItemList__value--id')]").click()
        select_dropdown_by_field_name(driver, "commentState", "Archived")
        wait_element_is_visible(driver, "//*[text()='Save']").click()
        wait_element_is_visible(driver, "//*[contains(@data-list-path,'comments')]").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        actualState = driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--select')]").text
        assert "Archived" in actualState
        assert originState != actualState

        delete_comment(driver)
        delete_post(driver)
        logout(driver)

    def delete_comment_on_admin_ui_page(self):
        print('---delete_comment_on_admin_ui_page---')
        driver = login()
        create_post(driver)
        create_comment(driver)

        wait_element_is_visible(driver, "//*[@class='octicon octicon-home']").click()
        wait_web_herf_is_visible(driver, "comments").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        wait_element_is_visible(driver, "//*[contains(@class,'ItemList__value--id')]/../preceding-sibling::*").click()
        wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
        wait_element_is_visible(driver, "//*[@data-button-type='confirm']").click()
        wait_element_is_visible(driver, "//*[text()='No comments found...']")
        noPosts = driver.find_element(By.XPATH, "//*[text()='No comments found...']").text
        assert "No comments found..." == noPosts

        delete_post(driver)
        logout(driver)

    def create_category_on_admin_ui_page(self):
        print('---create_category_on_admin_ui_page---')
        driver = login()

        wait_plus_icon_is_visible(driver, 'Posts', 'categories').click()
        wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
        input_text(driver, "//*[@name='name']", "CreateCategory")
        wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(driver, "//*[contains(@data-list-path,'categories')]").click()
        wait_element_is_visible(driver, "//*[@class='ItemList-wrapper']")
        assert "CreateCategory" in driver.find_element(By.XPATH, "//*[contains(@class,'ItemList__value--text')]").text

        delete_category(driver)
        logout(driver)

    def show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page(self):
        print('---show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page---')
        driver = login()
        create_category(driver)
        logout(driver)
        driver = login()

        wait_element_is_visible(driver, "//*[@class='octicon octicon-home']").click()   #createData
        wait_plus_icon_is_visible(driver, 'Posts', 'posts').click()
        wait_element_is_visible(driver, "//*[@data-screen-id='modal-dialog']")
        input_text(driver, "//*[@name='name']", "CreatePost")
        wait_element_is_visible(driver, "//*[@data-button-type='submit']").click()
        wait_element_is_visible(driver, "//*[@class='css-1r0jf0q item-name-field']")
        expectResult = driver.find_element(By.XPATH, "//*[@class='css-1r0jf0q item-name-field']").get_attribute("value")
        select_dropdown_by_field_name(driver, "state", "Published")
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@class='Relationships']")).perform()
        select_dropdown_by_field_name(driver, "categories", "CreateCategory")
        wait_element_is_visible(driver, "//*[@class='css-2960tt']")
        wait_element_is_visible(driver, "//*[text()='Save']").click()

        wait_element_is_visible(driver, "//*[@class='octicon octicon-sign-out']").click()   #logout
        wait_element_is_visible(driver, "//*[@class='auth-box__brand']").click()
        wait_element_is_visible(driver, "//li//*[text()='Blog']").click()
        wait_element_is_visible(driver, "//*[@class='badge pull-right']").click()

        actualResult = driver.find_element(By.XPATH, "//*[@class='media-heading']").text
        assert actualResult == expectResult

        driver.quit()
        driver = login()
        wait_web_herf_is_visible(driver, "posts").click()
        delete_post(driver)
        delete_category(driver)
        logout(driver)

    def create_enquiry_on_the_contact_page(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:3000/")
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

    suite.addTests([test_suite('create_post_on_the_admin_ui_page'),
                    test_suite('edit_post_on_the_admin_ui_page'),
                    test_suite('search_posts_by_keyword_on_the_admin_ui_page'),
                    test_suite('delete_post_on_the_admin_ui_page'),
                    test_suite('create_comment_on_admin_ui_page'),
                    test_suite('edit_comment_on_admin_ui_page'),
                    test_suite('delete_comment_on_admin_ui_page'),
                    test_suite('create_category_on_admin_ui_page'),
                    test_suite('show_posts_of_the_specific_category_by_pressing_category_name_on_the_blog_page'),
                    test_suite('create_enquiry_on_the_contact_page'),
                    test_suite('delete_enquiry_on_admin_ui_page'),
                    # test_suite('create_a_new_user_on_admin_ui_page')
                    ])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())