import unittest
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome()
        
    def test_a_update_personal_details(self): 
        # steps
        #open web browser
        browser = self.browser
        #open website
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        #input username
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        #input password
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        #click login
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
        #click My Info sidebar
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))).click()
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys([Keys.BACKSPACE] * 20)
        #input first name
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Nikolai")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "middleName"))).send_keys([Keys.BACKSPACE] * 20)
        #input input middle name
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "middleName"))).send_keys("Vladimir")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys([Keys.BACKSPACE] * 20)
        #input last name
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("Binkowsi")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input username
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input"))).send_keys("Makarov")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Employee Id
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"))).send_keys("123123123")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Other Id
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"))).send_keys("123321123")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Driver's License Number
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"))).send_keys("D6779SAW")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input License Expiry Date
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input"))).send_keys("1999-12-12")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input SSN Number
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input"))).send_keys("12345678")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input SIN Number
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input"))).send_keys("12354312")
        #input Nationality
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div"))).click()
        #click Indonesia
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[81]"))).click()
        #Click Marital Status
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div"))).click()
        #click Single
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]"))).click()
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/input"))).send_keys([Keys.BACKSPACE] * 10)
        #input Date of Birth
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/input"))).send_keys("2004-05-09")
        #click save
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"))).click()
      
        # validasi
        self.assertEqual(
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(.,'Successfully Updated')]"))).text,
            "Successfully Updated",
            "User berhasil disimpan"
        )
        
    def test_b_update_contact_details(self): 
        # steps
        #open web browser
        browser = self.browser
        #open website
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        
        #input username
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        #input password
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        #click login
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
        #click My Info sidebar
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))).click()
        #click Contact Details
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a"))).click()
        #input Street 1
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"))).send_keys("jalan")
        #input Street 2
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"))).send_keys("rambutan")
        #input City
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input"))).send_keys("Berlin")
        #input State/Province
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input"))).send_keys("Kremlin")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Zip/Postal Code
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input"))).send_keys("405345")
        #select Country
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div"))).click()
        #select Indonesia
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[101]"))).click()
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Home Telephone Number
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input"))).send_keys("123098123")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Mobile Telephone Number
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"))).send_keys("123321222")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Other Telephone Number
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"))).send_keys("123333333")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Work Email
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input"))).send_keys("openheimen@email.com")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Other Email
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input"))).send_keys("asdlkajsldkl@email.com")
        time.sleep(3)
        #click Save
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"))).click()
      
        # validasi
        self.assertEqual(
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(.,'Successfully Updated')]"))).text,
            "Successfully Updated",
            "User berhasil disimpan"
        )
        
    def test_c_emergency_contact(self): 
        # steps
        #open web browser
        browser = self.browser
        #open website
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #input username
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        #input password
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        #click login
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
        #click My Info sidebar
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))).click()
        #click Emergency Contact submenu
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a"))).click()
        #click Add Contact
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button"))).click()
        #input Name
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"))).send_keys("janjong")
        #input Relationship
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"))).send_keys("father")
        #input Home Telephone
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input"))).send_keys("123123321")
        #input Mobile Telephone
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"))).send_keys("123333333")
        #input Other Telephone
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"))).send_keys("111111111")
        #click save
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]"))).click()
      
        # validasi
        self.assertEqual(
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(.,'Successfully Saved')]"))).text,
            "Successfully Saved",
            "User berhasil disimpan"
        )
        
    def test_d_dependents(self): 
        # steps
        #open web browser
        browser = self.browser
        #open website
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #input username
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        #input password
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        #click login
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
        #click My Info sidebar
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))).click()
        #click Dependants submenu
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a"))).click()
        #click Add Dependants
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button"))).click()
        #input Name
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"))).send_keys("janjong")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]"))).send_keys([Keys.BACKSPACE] * 20)
        #input Date of Birth
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]"))).send_keys("1999-12-12")
        #select Relationship
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div"))).click()
        #select Other
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]"))).click()
        #input Specific Relationship
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input"))).send_keys("Brothers")
        #click Save
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]"))).click()
      
        # validasi
        self.assertEqual(
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(.,'Successfully Saved')]"))).text,
            "Successfully Saved",
            "User berhasil disimpan"
        )
        
    def test_d_qualifications(self): 
        # steps
        #open web browser
        browser = self.browser 
        #open website
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        #input username
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        #input password
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        #click login
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
        #click My Info sidebar
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))).click()
        #click Qualifications submenu
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a"))).click()
        #Click Add Work Experiences
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button"))).click()
        #input Company
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"))).send_keys("janjong")
        #input Job Title
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"))).send_keys("janjong")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Work Experience Start From
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input"))).send_keys("1999-12-12")
        #remove current input
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input"))).send_keys([Keys.BACKSPACE] * 20)
        #input Work Experience End to
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input"))).send_keys("2000-12-12")
        #input Comment
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[3]/div/div/div/div[2]/textarea"))).send_keys("Lorem Ipsum Dolor Sit Amet")
        #click save
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[4]/button[2]"))).click()
      
        # validasi
        self.assertEqual(
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(.,'Successfully Saved')]"))).text,
            "Successfully Saved"
        )
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()