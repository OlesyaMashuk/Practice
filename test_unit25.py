import pytest
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/driver/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()

def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('fox-cherry@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('Splm221081')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Выбираем питомцев пользователя
   pytest.driver.find_element_by_link_text('Мои питомцы').click()

   driver = webdriver.Chrome()
   driver.implicity_wait(10) #неявные ожидания

   wait = WebDriverWait(driver, 10)
   elements = wait.until(EC.presence_of_all_elements_located((By.ID, "all_my_pets"))) #явные ожидания

   #Количество питомцев в блоке статистики пользователя
   statistics = int((pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split())[2])
   # Определяем список с кол-вом карточек питомцев
   descriptions = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//tbody/tr')
   # получаем кол-во питомцев с фотогр
   images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//img')
   #получаем питомцев с именами
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')
   name_true = []
   for i in names:
       name_true.append(i.text)

   assert len(list(name_true)) == len(set(name_true)) #проверяем уникальность имен (тест не пройдет)
   assert statistics == len(descriptions) #присутствие всех питомцев

   for i in range(len(names)):
       assert images[i].get_attribute('src') != '' #проверка наличия фотографий у всех питомцев
       assert statistics == len(images) #хотя бы у половины питомцев есть фото
       assert names[i].text != '' #все питомцы имеют имя
       assert descriptions[i].text != '' #все карточки заполнены
       assert statistics == len(names) #все питомцы имеют имя возраст и породу
       assert elements != 1










