import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TS_ADD_USERNAME(unittest.TestCase):
    
    #Fungsi untuk configurasi webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./Belajar QA/chromedriver.exe")     
        
    #fungsi Login sukses
    def test_page_admin(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3) 

        #Input Username, password dan klik button Login
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
    
        #Memvalidasi apakah element yang tampil setelah klik Login merupakan elemen text Dashboard
        self.assertEqual(
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//div[@id='app']/div/div/header/div/div/span/h6"))).text,
        'Dashboard'
        )         

        #Membuka halaman admin
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(3) 
        driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/button").click()
        time.sleep(3) 
        
        
        #Input Value User Role
        driver.find_element(By.XPATH, "//div[2]/i").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "oxd-select-text-input").click()
        time.sleep(3)
        
        #select = driver.find_element(By.CLASS_NAME, "oxd-select-text-input")
        #drop = Select(select)
        
        #drop.select_by_visible_text("Admin")
        #time.sleep(3)
        
        #Input Value Employee Name
        driver.find_element(By.XPATH, "//div/div[2]/div/div/input").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div/div[2]/div/div/input").send_keys('Odis Adalwin')
        time.sleep(3)
        
        #response_data = driver.find_element(By.XPATH,"//div/div[2]/div/div/input").text
        #self.assertEqual(response_data, "Odis Aldawin")
        
        #Input Value Status
        driver.find_element(By.XPATH, "//div[3]/div/div[2]/div/div/div[2]/i").click()
        #time.sleep(3)
        #driver.find_element(By.CLASS_NAME, "oxd-select-text-input").click()
        #time.sleep(3)
        
        #Input Value Username
        driver.find_element(By.XPATH, "//div[2]/input").send_keys("Testing ARM")
        time.sleep(3)
        
        #Input Value Password
        driver.find_element(By.XPATH, "//div[2]/div/div/div/div[2]/input").send_keys("Password@12")
        time.sleep(3)
        
        
        #Input Value Confirm Password
        driver.find_element(By.XPATH, "//div[2]/div/div[2]/input").send_keys("Password@12")
        time.sleep(3)
        
        
if __name__ == "__main__":   
    unittest.main()
