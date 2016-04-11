from selenium import webdriver
from hacker_news import HackerNews
import csv


def extract_top_news():
    """ scrape all top news from the hacker news website """
    data = []
    driver = webdriver.Firefox()
    driver.get('https://news.ycombinator.com/')
    element_list = driver.find_elements_by_css_selector(HackerNews.title_url)
    for element in element_list:
        try:
            title_url = (element.text.encode('ascii', 'replace'), element.get_attribute('href').encode('ascii', 'replace'))
            data.append(title_url)
        except Exception as e:
            print e
    headers = ('Title', 'Title_URL')
    with open('write_data_1.csv', 'w+') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(headers)
        writer.writerows(data)
    driver.quit()

if __name__ == '__main__':
    extract_top_news()
