from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Selenium.form_test import TRForm

serv = Service("C:/Users/patri/Documents/Coding/RevTraining/Python/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=serv)

tr_form = TRForm(driver)


def _test():
    try:
        driver.get("file:///C:/Users/patri/Documents/Coding/RevTraining/Python/TuitionFE/employeedash.html")
        sleep(.5)

        tr_form.emp_id_input().send_keys("18")
        sleep(.5)

        tr_form.event_type_input().send_keys("1")

        tr_form.cost_input().send_keys("545")
        sleep(.5)

        tr_form.grade_input().send_keys("A")
        sleep(.5)

        tr_form.date_input().send_keys("05/13/2022")
        sleep(.5)

        tr_form.location_input().send_keys("L St")
        sleep(.5)

        tr_form.submit_button().click()
        sleep(1)

    except AssertionError as e:
        print(f"Test: Failed")
    else:
        print(f"Test Form Submission - Passed")

    driver.quit()


if __name__ == '__main__':
    _test()

