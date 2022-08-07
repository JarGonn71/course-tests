from selenium import webdriver
from selenium.webdriver.common.by import By


class Complex:
    def __init__(self, url):
        driver = webdriver.Chrome(executable_path="lib/chromedriver")
        driver.get(url)
        self.mydrive = driver

    def getElement(self, element):
        return self.mydrive.find_element(By.XPATH, element)
