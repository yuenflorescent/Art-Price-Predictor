from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('path/to/chromedriver')

class artsydriver:
    def __init__(self):
        self.driver = webdriver.Chrome('path/to/chromedriver')
    
    def getArtistPrediction(self, artist, year: 2024):
        driver = self.driver
        driver.get(f"https://www.artsy.net/artist/{artist}")
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
        prices = driver.find_elements(By.XPATH, "//*[@id='Sticky__ArtworkFilter']/div[3]/div[7]/div/div/div[2]/div[1]/div[1]/a/div/div[3]/div")
        
# for h in driver.window_handles:
#     driver.switch_to.window(h)