from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

class TestLogin(unittest.TestCase):
        #Membuka browser
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        #login
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)
        #modul TIME
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click() #timesheet
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]/a").click() #timesheet_employee_timesheet
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Paul") #employee_name
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div[2]/div/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(5)
        
driver.close()
driver.quit()
print('Test Completed')
        