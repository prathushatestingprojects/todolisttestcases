# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# connecting to chrome webdriver for selenium
s = Service('C:\webdriver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# max chrome window size
driver.maximize_window()
# search for url
driver.get("https://todo.scriveqa.com/")
# program contains 3 test cases:
# use case 1 for adding a new item in the list
# use case 2 for searching the list
# use case 3 to check the completed list
while True:
    # error handling
    try:
        case = int(input("Enter case no.: "))
        if case > 3 or case < 1:
            print("Please enter in range 1 to 3")
            continue
        # case 1 for adding list
        if case == 1:
            while True:
                driver.get("https://todo.scriveqa.com/")
                time.sleep(0.5)
                listname = input("Enter list name to add: ")
                if len(listname) > 1:
                    # click "+" add sign
                    plus = driver.find_element(By.XPATH, '//a[@title="Add New"]')
                    time.sleep(0.5)
                    # enter list name and press enter to add
                    add = driver.find_element(By.XPATH, '//input[@type="text"]')
                    add.click()
                    add.send_keys(listname)
                    add.send_keys(Keys.ENTER)
                    listname = ""
                    break
        # enter the listname below and press enter every time you want to add new list
        # 2 search list name
        if case == 2:
            while True:
                listname = input("Enter list name to search: ")
                driver.get("https://todo.scriveqa.com/")
                time.sleep(0.5)
                if len(listname) > 1:
                    # click on the search symbol
                    plus = driver.find_element(By.XPATH, '//a[@title="Search"]')
                    plus.click()
                    time.sleep(0.5)
                    # entering text and press enter to search
                    add = driver.find_element(By.XPATH, '//input[@type="text"]')
                    add.click()
                    add.send_keys(listname)
                    add.send_keys(Keys.ENTER)
                    listname = ""
                    break
        # Check the completed list
        if case == 3:
            while True:
                listname = input("Enter the completed list name to mark it as completed: ")
                driver.get("https://todo.scriveqa.com/")
                time.sleep(0.5)
                if len(listname) > 1:
                    # check the list that is completed
                    path = '//*[text()="' + listname + '"]'
                    plus = driver.find_element(By.XPATH, path)
                    plus.click()
                    listname = ""
                    break
    except:
        print("Please Enter correct details :")
        continue
