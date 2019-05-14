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