from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import textract
import random
import string
import os
import re


def indexer(url):
    tempname = ''.join(random.choice(string.ascii_uppercase)
                       for i in range(10))
    tempname = tempname + ".html"
    browser = webdriver.PhantomJS()
    browser.get(url)
    WebDriverWait(browser, 7)
    page_source = browser.page_source
    u = page_source.encode("utf-8")
    file = open('/tmp/%s' % (tempname), "w")
    file.write(u)
    file.close()
    text = textract.process('/tmp/%s' % (tempname))
    os.remove('/tmp/%s' % (tempname))
    text = text.replace('\r\n', '')
    text = text.replace('\n', '')
    text = text.replace('    ', '')
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text
