# pytest --language=es c:\Users\EL\selenium_course\module3lesson6final\test_items.py
# pytest --language=fr c:\Users\EL\selenium_course\module3lesson6final\test_items.py
# pytest c:\Users\EL\selenium_course\module3lesson6final\test_items.py

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_openSpanish(browser):
    browser.get(link)
    #time.sleep(30)
    message = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert "Añadir al carrito" == message.text, "Something went wrong :)"

if __name__ == "__main__":
        unittest.main()
        