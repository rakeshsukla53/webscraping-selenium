from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hack_nyu import HackNNYU
from selenium.webdriver.common.action_chains import ActionChains


def wait_until_visible_then_click(driver, element):
    element_signup = WebDriverWait(driver, 5, poll_frequency=.2).until(
        EC.visibility_of(element))
    element_signup.click()


def fill_up_hack_nyu():
    driver = webdriver.Firefox()
    driver.get('http://hacknyu.org/signup')
    driver.find_element_by_css_selector(HackNNYU.first_name).send_keys('Sean')
    driver.find_element_by_css_selector(HackNNYU.last_name).send_keys('DRosaeri')
    driver.execute_script("window.scrollTo(0, 300);")
    driver.find_element_by_css_selector(HackNNYU.email).send_keys('sukla.rakesh123@gmail.com')
    driver.find_element_by_css_selector(HackNNYU.password).send_keys('123456')
    driver.find_element_by_css_selector(HackNNYU.agree_checkbox).click()
    driver.find_element_by_css_selector(HackNNYU.accept_button).click()
    # driver.execute_script("window.scrollTo(0, 400);")
    driver.find_element_by_css_selector(HackNNYU.sign_up_button).click()
    # hover = ActionChains(driver).move_to_element(element)
    # hover.double_click()
    # hover.click_and_hold(element)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # element.click()
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, HackNNYU.accept_button)))
    # sleep(5)

fill_up_hack_nyu()
