from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from time import sleep


def get_credential():
    with open('functions/credential.json', 'r') as json_file :
        cred = json.load(json_file)
    return cred


def get_pages():
    with open('functions/pages.json', 'r') as json_file :
        pg = json.load(json_file)
        search_bar = driver.find_element_by_xpath('').click()
    return pg


def instagram():
    driver = webdriver.Chrome('functions/chromedriver')
    data = get_credential()
    driver.get('https://instagram.com')
    sleep(1)
    login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    login.click()
    sleep(1)
    login.send_keys(data['login'])
    password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    password.click()
    sleep(1)
    password.send_keys(data['pass'])
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    
    sleep(30)




instagram()