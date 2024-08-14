from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Ścieżka do geckodriver
driver_path = 'D:/SwagLabGUITesting/geckodriver.exe'  

# Ustawienia FirefoxOptions
options = Options()
service = Service(driver_path)

# Inicjalizacja WebDrivera z podaną ścieżką
driver = webdriver.Firefox(service=service, options=options)

# Otwórz stronę Google
driver.get('https://www.google.com')

# Wypisz tytuł strony
print(driver.title)

# Zamknij przeglądarkę
driver.quit()
