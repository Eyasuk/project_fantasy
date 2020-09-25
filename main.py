from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
PATH = r"C:\Users\user42\Desktop\gethub\project_fantasy\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://users.premierleague.com")
email="eyasukibru290@gmail.com"
passw="startover123"
try:
    submit=WebDriverWait(driver,100).until(
        EC.presence_of_element_located((By.CLASS_NAME,"btn-primary"))
        )
    username=driver.find_element_by_id("ism-email")
    password=driver.find_element_by_id("ism-password")
    username.send_keys(email)
    password.send_keys(passw)
    submit.send_keys(Keys.RETURN)
    fantasy_page=WebDriverWait(driver,100).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Play Fantasy Premier League"))
        )
    fantasy_page.send_keys(Keys.RETURN)
    
except:
    driver.quit()
 

