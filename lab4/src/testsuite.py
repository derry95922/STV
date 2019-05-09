import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:3000/")

def wait_element_is_visible(locate, timeout=5):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locate)))
    except Exception:
        driver.close()
    finally:
        return element

def wait_plus_icon_is_visible(title, subtitle, timeout=5):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-section-label='%s']//*[@data-list-path='%s']//a[@title='Create']" % (title, subtitle))))
    except Exception:
        driver.close()
    finally:
        return element

def input_text(locate,text):
    try:
        driver.find_element_by_xpath(locate).send_keys(text)
    except Exception:
        driver.close()    

def login():
    admin = {'account':'demo@keystonejs.com','password':'demo'}
    driver.maximize_window()
    wait_element_is_visible("//*[text()='Sign in']").click()
    input_text("//*[@name='email']",admin['account'])
    input_text("//*[@name='password']",admin['password'])
    wait_element_is_visible("//*[text()='Sign In']").click()
    wait_element_is_visible("//div[text()='Demo']")

'''Create post on the Admin UI page'''
try:
    login()
    sleep(1)
    wait_plus_icon_is_visible('Posts','posts').click()
    sleep(1)
    input_text("//*[@name='name']","dora")
    wait_element_is_visible("//*[@data-screen-id='modal-dialog']")
    wait_element_is_visible("//*[@data-button-type='submit']").click()
    wait_element_is_visible("//*[text()='Save']").click()
    sleep(1)
    assert "Your changes have been saved successfully" in driver.page_source
    wait_element_is_visible("//*[@data-list-path='posts']").click()
    sleep(1)
    assert "CreatePost" in driver.page_source
    
finally:
    sleep(1)
