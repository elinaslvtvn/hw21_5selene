#тут хранятся фикстуры
import pytest
from selene import browser


@pytest.fixture(scope = 'function', autouse=True)
def browser_open():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.timeout = 15
    yield
    browser.quit()