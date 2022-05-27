#!/usr/bin/env python

from __future__ import unicode_literals
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeWebDriver():

    def __init__(self) -> None:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def get_driver(self):
        return self.driver


def main():
    driver = ChromeWebDriver().get_driver()

    url = 'https://duckduckgo.com'

    driver.get(url)
    time.sleep(5)

    filename =  re.sub(r'[^a-zA-Z0-9]','_', url)
    driver.save_screenshot(f'{filename}.png')

    driver.quit()

main()