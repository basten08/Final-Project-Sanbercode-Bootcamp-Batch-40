import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

class TestLogin(unittest.TestCase):
        #Membuka browser
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        #login
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") #input username
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") #input password
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #buttton login
        time.sleep(10)
        #Membuka Modul TIME
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click() # modul TIME
        time.sleep(3)
        #Membuka Menu Project Info
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click() #menu Project Info
        time.sleep(1)
        #membuka submenu Customers
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]/a").click() #submenu Projects
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("ACME") #input customer name
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/span").click() #get value
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("ACME") #input project
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span").click() #get value
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div/div[2]/div/div/input").send_keys("test") #input project admin
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/span").click() #get value
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #button search
        time.sleep(2)
        
        
driver.close()
driver.quit()
print('Test Complited')