import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    pytest_driver.get('http://petfriends.skillfactory.ru/login')

    yield pytest_driver

    pytest_driver.quit()

def test_all_pet_friends():

   # неявное ожидание
   pytest_driver.implicitly_wait(10)

   # Вводим email
   pytest_driver.find_element_by_id('email').send_keys('9169868008@mail.ru')
   time.sleep(3)
   # Вводим пароль
   pytest_driver.find_element_by_id('pass').send_keys('Stens2022')
   time.sleep(3)
   # Нажимаем на кнопку входа в аккаунт
   pytest_driver.find_element_by_css_selector('button[type="submit"]').click()
   time.sleep(3)
   # Нажимаем на кнопку Мои питомцы
   pytest_driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
   time.sleep(3)
   images = pytest_driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest_driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest_driver.find_elements_by_css_selector('.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
