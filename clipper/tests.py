from django.test import TestCase
from requests.compat import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
# Create your tests here.
BASE_URL = "https://nomadcoders.co/"

def get_title():

    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get(BASE_URL)
        title = browser.find_element_by_xpath('//title')

        html = title.get_attribute("innerHTML")
        soup = BeautifulSoup(html, 'lxml')
        print('스크레이핑에 성공하였습니다.')
    return soup.get_text()

