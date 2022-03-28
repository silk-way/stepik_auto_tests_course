from selenium import webdriver
import time
import math
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button = browser.find_element_by_id("book")
    button.click()
    option1 = browser.find_element_by_id("input_value")
    prelim1=option1.text
    print(prelim1)
    y = calc(prelim1)
    print(y)
    option2 = browser.find_element_by_css_selector("#answer")
    option2.send_keys(y)
    button2 = browser.find_element_by_id("solve")
    button2.click()

    #message = browser.find_element_by_id("verify_message")

    #assert "successful" in message.text
    #time.sleep(1)
    #button = browser.find_element_by_css_selector(".trollface")
    #button.click()
    #confirm = browser.switch_to.alert
    #confirm.accept()
    #time.sleep(2)
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    #option1 = browser.find_element_by_id("input_value")
    #prelim1=option1.text
    #print(prelim1)
    #y = calc(prelim1)
    #option2 = browser.find_element_by_css_selector("#answer")
    #option2.send_keys(y)
    #option1_2 = browser.find_element_by_id("num2")
    #prelim2=option1_2.text
    #print(prelim1)
    #y=str(int(prelim1)+int(prelim2))
    #y=calc(prelim1)
    #print(y)


    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(y)  # ищем элемент с текстом "Python"
    #option1_2 = browser.find_element_by_css_selector("#answer")
    #option1_2.send_keys(y)
    #browser.execute_script('button = document.getElementsByTagName("input")[0];button.scrollIntoView(true);')
    #option2 = browser.find_element_by_css_selector("#robotCheckbox") #input_value
    #option2.click()
    #option3 = browser.find_element_by_css_selector("[value='robots']")
    #option3.click()

    #input1 = browser.find_element_by_name('firstname')
    #input1.send_keys("Anton")
    #input2 = browser.find_element_by_name('lastname')
    #input2.send_keys("Anton")
    #input3 = browser.find_element_by_name('email')
    #input3.send_keys("Anton@anton.uz")
    
    #current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    #file_path = os.path.join(current_dir, 'myfile.txt')  # добавляем к этому пути имя файла
    #print(current_dir, file_path)
    #input4 = browser.find_element_by_id("file")
    #input4.send_keys(file_path)
    #input1 = browser.find_element_by_css_selector('input.first[required]') # Ищем поле ввода (input) с классом
    #input1.send_keys("Anton")                                              # first и атрибутом тега required
    #input2 = browser.find_element_by_css_selector('input.second[required]')# Так мы делаем три раза подряд.
    #input2.send_keys("Anton")                                              # Если количество полей изменилось,
    #input3 = browser.find_element_by_css_selector('input.third[required]') # то тест дальше не идёт и выпадает с
    #input3.send_keys("anton@anton.uz")                                     # требуемой ошибкой NoSuchElementException
    # Конец решения

    # Отправляем заполненную форму
    #browser.execute_script('button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);')
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()