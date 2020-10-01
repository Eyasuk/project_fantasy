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
league_no="142197"
standings="https://fantasy.premierleague.com/leagues/"+league_no+"/standings/c"
player_no=30
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
    driver.get(standings)
    table=WebDriverWait(driver,110).until(
        EC.presence_of_element_located((By.TAG_NAME,"table"))
        )
    table_body=table.find_element_by_tag_name("tbody")
    table_rows=table_body.find_elements_by_tag_name("tr")
    for table_row in table_rows:
        datas=table_row.find_elements_by_class_name("GxMKk")
        for data in datas:
            print(data.text+"")
            
     
    
except:
    driver.quit()
 

