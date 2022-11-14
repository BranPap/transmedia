import time
import csv

from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

SCROLL_PAUSE_TIME = 3

headers = ["title","url"]

if __name__=='__main__':

    options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome("/mnt/c/Users/Administrator/Documents/chromedriver", options=options) 
    driver.get("https://www.pinknews.co.uk/?s=transgender")
    time.sleep(3)


    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    with open("urls.csv","w",newline="") as csvOutput:
        w = csv.writer(csvOutput)
        # w.writerow(headers)
        

        for _ in range(400): # scroll N times --> change here how much you want to scroll down
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        elements = driver.find_elements(By.CLASS_NAME, 'latest-posts-section__post-single')
        links = driver.find_elements(By.XPATH, "//div[@class='latest-posts-section__post-single']/a")

        texts = []
        urls = []

        for elem in elements:
            if 'SPONSORED CONTENT' not in elem.text: # this messes up the order in texts and urls lists (by filtering these we can print the text that goes with an url as below)
                texts.append(elem.text)

        for link in links:
            urls.append(link.get_attribute("href"))

        for text, url in zip(texts, urls):
            w.writerow([url])
           
        time.sleep(3)
        