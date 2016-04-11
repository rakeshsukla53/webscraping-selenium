from selenium import webdriver
from brain_quote_page import BrainQuotePage


def extract_donald_trump_quotes():
    browser = webdriver.Firefox()
    browser.get('http://www.brainyquote.com/quotes/authors/d/donald_trump.html')
    while True:
        try:
            all_quotes = browser.find_elements_by_css_selector(BrainQuotePage.donald_trump_quotes)
            all_quote_links = browser.find_elements_by_css_selector(BrainQuotePage.donald_trump_links)
            for quotes, quote_link in zip(all_quotes, all_quote_links):
                # donald trump quote and link
                print (quotes.text, quote_link.get_attribute('href'))
            next_page = browser.find_element_by_css_selector(BrainQuotePage.donald_trump_next_page)
            next_page.click()
        except:
            # we have reached the last page
            break
    browser.quit()

if __name__ == '__main__':
    extract_donald_trump_quotes()