import os
from selene import browser , be , have


def test_add_form_selene():
    browser.element('[name="firstName"]').type('Имя')
    browser.element('#lastName').type("Фамилия")
    browser.element('userEmail').type("test@gmail.com")
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type("+79991234567")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').should(be.visible).click()
    browser.element('option[value="1995"]').should(be.visible).click()
    browser.element('.react-datepicker__day react-datepicker__day--001 react-datepicker__day--weekend').click()
    browser.element('#subjectsInput').type("Maths").press_enter()
    browser.element('label[for ="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_file.txt'))
    browser.element('#currentAddress').type('Address')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('[id = "example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

