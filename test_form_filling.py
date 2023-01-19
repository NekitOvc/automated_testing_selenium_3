from selenium.webdriver.common.by import By
from test_options import testing, get_chrome_options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import one_thousand_characters, name, password
from random import randint

import time
import requests
import random


# TEST_01
# проверка, что пользователь может успешно перейти на сайт
def test_opening_page(testing):
    selenium = testing
    url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
    selenium.get(url)
    response = requests.get(url)

    # ожидание элемента на странице
    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    selenium.save_screenshot('test_opening_page.png')

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Basic HTML Form Example', print('Тест провален')
    assert response.status_code == 200, print('Тест провален')


# TEST_02
# проверка заполнения полей на 1000 символов
def test_one_thousand_characters(testing):
    selenium = testing
    selenium.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')

    # ожидание элемента на странице
    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        print('Элемент отобразился')
    except:
        print('Элемент не отобразился')

    # ввод данных в поле "Username"
    selenium.find_element(By.NAME, 'username').send_keys(one_thousand_characters)
    time.sleep(1)
    # ввод данных в поле "Password"
    selenium.find_element(By.NAME, 'password').send_keys(one_thousand_characters)
    time.sleep(1)
    # в поле "TextArea Comment":
    # выделить текст
    selenium.find_element(By.NAME, 'comments').send_keys(Keys.CONTROL + 'A')
    time.sleep(1)
    # удалить текст
    selenium.find_element(By.NAME, 'comments').send_keys(Keys.DELETE)
    time.sleep(1)
    # заполнить новым текстом
    selenium.find_element(By.NAME, 'comments').send_keys(one_thousand_characters)
    time.sleep(1)

    # нажать на кнопку "submit"
    selenium.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/input[2]').click()
    time.sleep(3)

    selenium.save_screenshot('test_one_thousand_characters.png')

    assert selenium.find_element(By.ID, '_valueusername').text == one_thousand_characters, print('Тест провален')
    assert selenium.find_element(By.ID, '_valuepassword').text == one_thousand_characters, print('Тест провален')
    assert selenium.find_element(By.ID, '_valuecomments').text == one_thousand_characters, print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Processed Form Details', print('Тест провален')


# TEST_03
# проверка заполнения полей "Username" и "Password" любыми данными
def test_filing_data(testing):
    selenium = testing
    selenium.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')

    # ожидание элемента на странице
    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.NAME, 'username')))
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))
        print('Элементы отобразились')
    except:
        print('Элементы отобразились')

    # сохранение рандомных данных в переменные
    test_name = random.choice(name)
    test_password = random.choice(password)

    selenium.find_element(By.NAME, 'username').send_keys(test_name)
    time.sleep(1)
    selenium.find_element(By.NAME, 'password').send_keys(test_password)
    time.sleep(1)

    # нажать на кнопку "submit"
    selenium.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/input[2]').click()
    time.sleep(3)

    selenium.save_screenshot('test_filing_data.png')

    assert selenium.find_element(By.ID, '_valueusername').text == test_name, print('Тест провален')
    assert selenium.find_element(By.ID, '_valuepassword').text == test_password, print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Processed Form Details', print('Тест провален')


# TEST_04
# проверка заполнения всех полей любыми данными
def test_all_filing_data(testing):
    selenium = testing
    selenium.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')

    # ожидание элемента на странице
    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.NAME, 'username')))
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))
        print('Элементы отобразились')
    except:
        print('Элементы отобразились')

    # сохранение данных из списка в переменные
    test_name = random.choice(name)
    test_password = random.choice(password)

    # заполнение поля "Username" любыми данными
    selenium.find_element(By.NAME, 'username').send_keys(test_name)
    time.sleep(1)
    # заполнение поля "Password" любыми данными
    selenium.find_element(By.NAME, 'password').send_keys(test_password)
    time.sleep(1)
    # заполнение поля "TextArea Comment" любыми данными
    selenium.find_element(By.NAME, 'comments').send_keys(test_name)
    time.sleep(1)
    # убрать значение "Checkbox 3" из поля "Checkbox Items" перед выбором нового пункта
    selenium.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[3]').click()
    time.sleep(1)
    # выбор любого пункта "Checkbox Items"
    selenium.find_element(By.XPATH, f'//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[{randint(1, 3)}]').click()
    time.sleep(1)
    # выбор любого пункта "Radio Items"
    selenium.find_element(By.XPATH, f'//*[@id="HTMLFormElements"]/table/tbody/tr[6]/td/input[{randint(1, 3)}]').click()
    time.sleep(1)
    # выбор любого пункта из поля "Multiple Select Values"
    selenium.find_element(By.XPATH, f'//*[@id="HTMLFormElements"]/table/tbody/tr[7]/td/select/option[{randint(1, 4)}]').click()
    time.sleep(1)
    # выбор любого значения из выпадающего списка "Dropdown"
    selenium.find_element(By.XPATH, f'//*[@id="HTMLFormElements"]/table/tbody/tr[8]/td/select/option[{randint(1, 6)}]').click()
    time.sleep(1)

    # сохраняем скрин введенных данных, чтобы иметь представление, что было введено в форму
    selenium.save_screenshot('test_all_filing_data_1.png')

    # нажать на кнопку "submit"
    selenium.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/input[2]').click()
    time.sleep(3)

    # скрин вывода
    selenium.save_screenshot('test_all_filing_data_2.png')

    assert selenium.find_element(By.ID, '_valueusername').text == test_name, print('Тест провален')
    assert selenium.find_element(By.ID, '_valuepassword').text == test_password, print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Processed Form Details', print('Тест провален')