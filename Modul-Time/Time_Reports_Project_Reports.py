import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

class TestLogin(unittest.TestCase):
        #Membuka browser
        driver.get("https://opensource-demo.orangehrmlive.com/") #buka situs
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") #isi valid email
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") #isi valid pass
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik button sign in
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span").click() #klik modul TIME
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() #klik menu Reports
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a").click() #klik submenu Project reports
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("ACME Ltd") #input kata kunci
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[1]/span").click() #get value
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input").click() # klik field date from
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[14]/div").click() #from date
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div/input").click() #klik field date to
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[16]/div").click() #to date
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/form/div[3]/button").click()
        time.sleep(3)
        
                
        driver.close()
        driver.quit()
        print('OK--Test Complited')

