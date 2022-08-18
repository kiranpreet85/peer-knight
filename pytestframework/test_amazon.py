import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = None
def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.com")
    driver.implicitly_wait(3)

def teardown_module(module):
    driver.quit()


def test_page_title():
    titleofthepage = driver.title
    assert titleofthepage == "Amazon.com. Spend less. Smile more."


def test_page_URL():
    url = driver.current_url
    assert url == "https://www.amazon.com/"

def test_page_logo():
    assert driver.find_element(By.ID,"nav-logo-sprites").is_displayed()

def test_page_login():
    driver.find_element(By.XPATH,"//*[@id='nav-link-accountList']").click()
    driver.find_element(By.ID,"ap_email").send_keys("ohm.upstate03@icloud.com")
    driver.find_element(By.ID,"continue").click()
    driver.find_element(By.ID,"ap_password").click()
    driver.find_element(By.ID,"ap_password").send_keys("Test1234$")
    driver.find_element(By.ID,"signInSubmit").click()
    assert "Your Amazon.com" == "Your Amazon.com"
