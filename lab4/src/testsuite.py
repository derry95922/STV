from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:3000/")

def wait_element_is_visible(locate, timeout=3):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, locate)))
    except Exception:
        driver.close()
    finally:
        return element

def wait_plus_icon_is_visible(title, subtitle, timeout=3):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-section-label='%s']//*[@data-list-path='%s']//a[@title='Create']" % (title, subtitle)))
        )
    except Exception:
        driver.close()
    finally:
        return element

def login():
    admin = {'account':'demo@keystonejs.com','password':'demo'}
    driver.maximize_window()
    wait_element_is_visible("//*[text()='Sign in']").click()
    driver.find_element_by_xpath("//*[@name='email']").send_keys(admin['account'])
    driver.find_element_by_xpath("//*[@name='password']").send_keys(admin['password'])
    wait_element_is_visible("//*[text()='Sign In']").click()

try:
    login()
    wait_plus_icon_is_visible('Posts','posts').click()
    sleep(3)
finally:
    driver.close()
