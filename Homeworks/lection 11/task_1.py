# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
about_page = 'https://tensor.ru/about'
driver = webdriver.Chrome()

try:
    driver.get(sbis_site)

    # кликаем по кнопке "Контакты"
    contact_btn = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    contact_btn.click()
    sleep(1)

    # кликаем по баннеру "Тензор"
    banner_tensor = driver.find_element(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    banner_tensor.click()
    sleep(1)

    # проверяем наличие блока с новостью "Сила в людях"
    driver.switch_to.window(driver.window_handles[1])
    news_block = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    assert news_block.is_displayed(), 'Новостной блок "Сила в людях отсутствует"'

    # кликаем по кнопке "Подробнее", проверяем URL
    more_btn = driver.find_element(By.CSS_SELECTOR, '[href="/about"]')
    more_btn.click()
    sleep(1)
    assert driver.current_url == about_page

finally:
    driver.quit()
