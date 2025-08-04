#тут хранятся фикстуры
import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope = 'function', autouse=True)
def browser_open():
    # browser.driver.execute_script("$('#fixedban').remove()")
    # browser.driver.execute_script("$('footer').remove()")
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.timeout = 4
    yield
    browser.quit()