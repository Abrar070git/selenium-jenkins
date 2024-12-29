import pytest
from selenium.webdriver.ie.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure

def setup_function():
    global driver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('https://stage.alnafi.com/')
    driver.maximize_window()

def teardown_function():
    driver.quit()

@pytest.mark.parametrize('username, password',[('am3030441@gmail.com' , 'sarah@gmail.com') ,('samira@gmail.com' , 'samira123')])
def test_func(username, password):
    driver.find_element(By.NAME, 'email').send_keys(username)
    time.sleep(5)
    driver.find_element(By.NAME,'password').send_keys(password)
    time.sleep(5)

    allure.attach(driver.get_full_page_screenshot_as_png(), name='Alnafi_sc' , attachment_type='AttachmentType.PNG')

############################################################################################
