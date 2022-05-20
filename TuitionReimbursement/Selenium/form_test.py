from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TRForm:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def emp_id_input(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/input[1]")

    def event_type_input(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/input[2]")

    def cost_input(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/input[3]")

    def grade_input(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/input[4]")

    def date_input(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/input[5]")

    def location_input(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/input[6]")

    def submit_button(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/button")
