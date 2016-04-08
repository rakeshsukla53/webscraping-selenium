from selenium import webdriver
from go_django import GoDjango
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


def download_videos():
    driver = webdriver.Firefox()
    driver.get('https://godjango.com/browse/')
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, GoDjango.first_video_title)))
    while True:
        for element in range(0, 10):
            all_video_elements = driver.find_elements_by_css_selector(GoDjango.first_video_title)
            all_video_elements[element].click()
            try:
                print driver.find_element_by_css_selector(GoDjango.video_download_link).get_attribute('src')
            except:
                print "Video is private"
            driver.execute_script("window.history.go(-1)")
            driver.execute_script("window.scrollTo(0, 465);")
        driver.execute_script("window.scrollTo(0, 4650);")
        sleep(2)
        driver.find_element_by_css_selector(GoDjango.next_button_click).click()
    driver.quit()

if __name__ == '__main__':
    download_videos()

