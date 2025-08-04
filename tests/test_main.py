import os
from selene import browser , be , have
def test_add_form_selene():
    browser.element('#firstName').type("Имя")
    browser.element('#lastName').type("Фамилия")
    browser.element('#userEmail').type("test@gmail.com")
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type("7999123456")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').should(be.visible).click()
    browser.element('option[value="1995"]').should(be.visible).click()
    browser.element('.react-datepicker__day.react-datepicker__day--001.react-datepicker__day--weekend').click()
    browser.element('#subjectsInput').type("Maths").press_enter()
    browser.element('label[for ="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_file.txt'))
    browser.element('#currentAddress').type("Address")

    browser.element('#state input').type('NCR').press_enter()




    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    #добавила проверки введенных полей после "Submit"
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Имя'))
    browser.element('.table').should(have.text('Фамилия'))
    browser.element('.table').should(have.text('test@gmail.com'))
    browser.element('.table').should(have.text('7999123456'))
    browser.element('.table').should(have.text('01 January,1995'))
    browser.element('.table').should(have.text('Maths'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('Address'))
    browser.element('.table').should(have.text('NCR Delhi'))
    browser.element('.table').should(have.text('test_file.txt'))
