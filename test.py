import subprocess
import sys


# Функция для установки недостающих библиотек
def install_packages():
    try:
        import selenium
        import bs4
        import webdriver_manager
    except ImportError:
        print("Устанавливаем недостающие библиотеки...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "selenium", "beautifulsoup4", "webdriver_manager"])


# Вызываем функцию установки пакетов
install_packages()

# Теперь можно импортировать библиотеки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def check_footer_elements():
    # Открываем браузер и загружаем страницу
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://only.digital/")

    # Получаем HTML-код страницы
    page_source = driver.page_source
    driver.quit()  # Закрываем браузер

    # Парсим HTML с помощью BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Проверяем наличие тега <footer>
    footer = soup.find('footer')
    footer_exists = footer is not None

    # Проверяем наличие текста "+7 (495) 740 99 79" в футере
    phone_exists = footer_exists and "+7 (495) 740 99 79" in footer.text

    # Проверяем наличие символа "©" в футере
    copyright_exists = footer_exists and "©" in footer.text

    # Выводим результаты в виде списка True/False
    return [footer_exists, phone_exists, copyright_exists]

#

# Запускаем проверку и выводим результат
result = check_footer_elements()
print(result)
