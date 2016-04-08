from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from time import sleep

# set the scrolling behavior to down
DesiredCapabilities.FIREFOX["elementScrollBehavior"] = 1


def fill_up_hack_nyu(student):
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    # load the page
    driver.get("http://hacknyu.org/signup")

    # get the form element
    form = driver.find_element_by_css_selector("form[name='signupForm']")

    # fill the fields
    form.find_element_by_css_selector("input[name='firstName']").send_keys(student['first_name'])
    form.find_element_by_css_selector("input[name='lastName']").send_keys(student['last_name'])
    form.find_element_by_css_selector("input[name='email']").send_keys(student['email_id'])
    form.find_element_by_css_selector("input[name='password']").send_keys("technyu")

    # click and accept terms
    form.find_element_by_xpath("//input[@name='terms']/..").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='Accept']"))).click()
    wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal")))

    # click on submit
    form.find_element_by_css_selector("button[type='submit']").click()
    driver.quit()


def read_csv_files():
    with open('data1.csv', 'r+') as data_file:
        data = csv.DictReader(data_file)
        for row in data:
            fill_up_hack_nyu(row)
            sleep(3)

read_csv_files()
