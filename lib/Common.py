from selenium import webdriver
from selenium.webdriver.common.by import By


class Common:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait_time = 5

    def set_driver(self, url: str) -> None:
        self.driver.get(url)
        self.driver.implicitly_wait(time_to_wait=self.wait_time)

    def get_driver(self) -> webdriver.Chrome:
        return self.driver

    def find_element(self, element: str) -> webdriver.Chrome.find_element:
        return self.driver.find_element(By.XPATH, element)
