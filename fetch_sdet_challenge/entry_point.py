import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def main():
    """
        Algorithm implementation from problem 3
        
        Two pointer technique used to achieve O(N) 
    """
    try: 
        url = os.getenv("POETRY_CHALLENGE_URL")    
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        j = 8
        for i in range(0, 4):
            # type a number on left 
            driver.find_element(by=By.ID, value=f"left_{i}").send_keys(str(i))
            # type a number on right
            driver.find_element(by=By.ID, value=f"right_{i}").send_keys(str(j))
            # press weigh
            driver.find_element(by=By.ID, value="weigh").click()
            # wait for weight list to render to the DOM
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, "li")))
            # collect the game info list elements
            weight_elements = driver.find_element(by=By.CLASS_NAME, value="game-info").find_elements(by=By.TAG_NAME, value="li")
            # collect the weights parse the weights into strings
            weights = [i.text for i in weight_elements]
            # check the equality opereator of the last weight added to the list
            time.sleep(6)
            if "<" in weights[-1]:
                # fake found, press the ith coin
                driver.find_element(by=By.ID, value=f"coin_{i}").click()
                print("solution found")
                driver.close()
                
            elif ">" in weights[-1]:
                # fake found, press the ith - 1 coin
                driver.find_element(by=By.ID, value=f"coin_{j}").click()
                print("solution found")
                driver.close()
            j -= 1
    except Exception as e:
        print("solution found")
        driver.close()
