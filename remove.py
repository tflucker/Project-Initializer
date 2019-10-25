import sys
import os
from os import path

from selenium import webdriver


# Replace with path where you want to save new projects
path = "/Git_Checkouts/"

# Github credentials
username = ""
password = ""

browser = webdriver.Chrome()
browser.get('https://github.com/login')

def remove():

    repo_name = username +'/'+ str(sys.argv[1])

    field = browser.find_element_by_xpath("//*[@id='login_field']")
    field.send_keys(username)

    field = browser.find_element_by_xpath("//*[@id='password']")
    field.send_keys(password)

    login_btn = browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
    login_btn.click()

    browser.get('https://github.com/'+repo_name+'/settings')

    button = browser.find_element_by_xpath('//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary')
    button.click()

    field = browser.find_element_by_xpath('//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')
    field.send_keys(repo_name)

    button = browser.find_element_by_xpath('//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')
    button.click()

if __name__ == "__main__":
	remove()
