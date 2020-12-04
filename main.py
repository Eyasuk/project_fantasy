from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Fantasy:
    def __init__(self,username,password,league_id):
        self.username=username
        self.password=password
        self.league_id=league_id
    def standing(self): 
        PATH = r"C:\Users\user42\Desktop\gethub\project_fantasy\chromedriver.exe"
        driver=webdriver.Chrome(PATH)
        driver.get("https://users.premierleague.com")
        standings="https://fantasy.premierleague.com/leagues/"+self.league_id+"/standings/c"
        try:
            submit=WebDriverWait(driver,100).until(
                EC.presence_of_element_located((By.CLASS_NAME,"btn-primary"))
                    )   
            username=driver.find_element_by_id("ism-email")
            password=driver.find_element_by_id("ism-password")
            username.send_keys(self.username)
            password.send_keys(self.password)
            submit.send_keys(Keys.RETURN)
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
                print("")
            
        except:
            driver.quit()
 
p=Fantasy("eyasukibru290@gmail.com","startover123","142197")
p.standing()