from selenium import webdriver
from feedback_form import HandyFeedbackForm
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


def fill_up_handy_feedback():
    driver = webdriver.Firefox()
    driver.get('https://handyproductteam.typeform.com/to/VLLmRX')
    sleep(2)
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, HandyFeedbackForm.start_button)))
    driver.find_element_by_xpath(HandyFeedbackForm.start_button).click()
    sleep(1)
    driver.find_element_by_xpath(HandyFeedbackForm.booking_id_text).send_keys('5432512')
    sleep(1)
    element = driver.find_element_by_xpath(HandyFeedbackForm.question_2_yes_button)
    print element.is_displayed()
    print element.is_enabled()
    print element.is_selected()
    element.click()
    driver.execute_script("arguments[0].class='container step0 selected'", element)
    print element.is_selected()
    driver.quit()
    # driver.find_element_by_xpath(HandyFeedbackForm.question_3_answer).click()
    # sleep(3)
    # driver.find_element_by_xpath(HandyFeedbackForm.question_4_answer).click()
    # sleep(3)
    # driver.find_element_by_xpath(HandyFeedbackForm.question_5_answer).click()
    # sleep(3)
    # driver.find_element_by_xpath(HandyFeedbackForm.question_6_answer).click()
    # sleep(3)
    # driver.find_element_by_xpath(HandyFeedbackForm.question_7_answer).send_keys("Spend more time on washroom and kitchen")
    # sleep(3)

if __name__ == '__main__':
    fill_up_handy_feedback()







