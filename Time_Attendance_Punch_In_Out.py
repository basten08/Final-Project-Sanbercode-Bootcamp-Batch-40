import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

class TestLogin(unittest.TestCase):
        #login
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)
        #open Modul TIME
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)
        #open menu Attendance
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
        time.sleep(1)
        #open submenu Punch In/Out
        #Punch In
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div/div/div/div[2]/textarea").send_keys("test awal1234") # input note
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button").click() # button In
        time.sleep(3)
        #Punch Out
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div/div/div/div[2]/textarea").send_keys("test akhir1234") #input note
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button").click() # button Out
        time.sleep(3)
        
        
        
driver.close()
driver.quit()
print('Test Completed')
        