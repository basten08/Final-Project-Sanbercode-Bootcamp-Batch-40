import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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
        
        #Membuka halaman admin
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        time.sleep(3) 

        #Cancel Delate  
        driver.find_element(By.CLASS_NAME,"oxd-icon-button oxd-table-cell-action-space").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[3]/div/div/div/div[3]/button").click()
        time.sleep(1)
        
if __name__ == "__main__":   
    unittest.main()
