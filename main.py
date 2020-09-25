from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
PATH = r"C:\Users\user42\Desktop\gethub\project_fantasy\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://users.premierleague.com")
username=driver.find_element_by_id("ism-email")
password=driver.find_element_by_id("ism-password")
submit=""
try:
    submit=WebDriveWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS,"btn-primary"))
        )
except:
    driver.quit()
    
print(submit.text)
