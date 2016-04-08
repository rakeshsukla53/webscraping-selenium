from selenium import webdriver
import csv

browser = webdriver.Firefox()
type(browser)
browser.get('http://www.brainyquote.com/quotes/authors/d/donald_trump.html')
data = []

while True:
    try:
        all_quotes = browser.find_elements_by_css_selector('span[class="bqQuoteLink"]')
        all_quote_links = browser.find_elements_by_css_selector('span[class="bqQuoteLink"] a')
        for quotes, quote_link in zip(all_quotes, all_quote_links):
            print (quotes.text, quote_link.get_attribute('href'))
        next_page = browser.find_element_by_css_selector('.pagination-sm .active + li a  ')
        next_page.click()
    except Exception as e:
        raise("Reached last page")

# headers = ('Donald Trump', 'Quotes')
# with open('write_data_1.csv', 'w+') as data_file:
#     writer = csv.writer(data_file)
#     writer.writerow(headers)
#     writer.writerows(data)

browser.quit()

