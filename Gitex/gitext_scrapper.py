from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

def listToString(list): 
    str_ = ""    
    for i in list:
        str_ += i + " - "     
    return str_

def gitex_scrapper():

    data = []
    # All data which is scrapped
    
    # Complete Div Tags

    try:

        options = webdriver.ChromeOptions()
        print('--------------------------------------Driver Installation------------------------------------------------')
        service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        print('--------------------------------------Driver Installation Completed--------------------------------------')
        driver = webdriver.Chrome(service=service,options=options)  
        driver.maximize_window()
        driver.implicitly_wait(5)

        #---------------------------------------------Anchor Tag -----------------------------------------------------
        url = f'https://exhibitors.gitex.com/gitex-global-2023/Exhibitor'
        driver.get(url)        
         

        #---------------------------------------------Anchor Tag-----------------------------------------------------
        # driver.find_element(By.XPATH,"//a[@id='alphabet_A']").click()
        # sleep(4)

        

        #---------------------------------------------Scroll the infinite page----------------------------------------
        print('--------------------------------------Scrolling Start----------------------------------------------------')
        reached_page_end = False
        last_height = driver.execute_script("return document.body.scrollHeight")        
        try:
            while not reached_page_end:        
                sleep(5)
                driver.find_element(By.XPATH,'//body').send_keys(Keys.END)                           
                new_height = driver.execute_script("return document.body.scrollHeight")                    
                if last_height == new_height:
                    reached_page_end = True
                else:
                    last_height = new_height
        except Exception as e:
            print(e)
        print('--------------------------------------Scrolling End------------------------------------------------------')        
        #---------------------------------------------Scroll the infinite page-------------------------------------
        lst = driver.find_elements(By.XPATH,"//div[@class='thumbnail ']")
        print('--------------------------------------Scrapping Start----------------------------------------------------')
        print(len(lst))
        for i in range(len(lst)):
            print(i)            
            #---------------------------------------------Address Name---------------------------------------------
            address = driver.find_elements(By.XPATH, '//h4[@class="heading"]')[i].text

            #---------------------------------------------Heading Title--------------------------------------------
            title = driver.find_elements(By.XPATH,"(//div[@class='web'])/p[1]")[i].text

            #---------------------------------------------Country Name---------------------------------------------
            country_name = driver.find_elements(By.XPATH,"(//div[@class='web'])/p[2]")[i].text

            #---------------------------------------------Description Title----------------------------------------
            description = driver.find_elements(By.XPATH,"(//div[@class='web'])/p[3]")[i].text
            
            #---------------------------------------------Tags-----------------------------------------------------
            tags = listToString( driver.find_elements(By.XPATH,"//div[@class='sector_block_outer']")[i].text.split("\n"))    

            #---------------------------------------------Profile link---------------------------------------------
            profile_link = driver.find_elements(By.XPATH,"//div[@class='button_block text-right']/a")[i].get_attribute('href')


            gitex_data = {
                "Address":address,
                "Title":title,
                "Country Name":country_name,
                "Description":description,
                "Tags": tags,
                "Profile Link":profile_link
            }
            
            data.append(gitex_data)        
            
        return data         
    
    except Exception as e:
        print(e)



# Driver Code
df = pd.DataFrame(gitex_scrapper())
df.to_csv('GitexData.csv')
