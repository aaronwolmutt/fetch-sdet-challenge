import logging

from fetch_sdet_challenge.driver import *
from selenium.webdriver.common.by import By

def main():
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    left_bowl = []
    right_bowl = []
    gold_bars = []

    # locating the buttons on the game boards and coins
    for i in range(0, 9):
        left_id = f"left_{i}"
        right_id = f"right_{i}"
        coin_id = f"coin_{i}"
        
        left_bowl.append(driver.find_element(by=By.ID, value=left_id))
        right_bowl.append(driver.find_element(by=By.ID, value=right_id))
        gold_bars.append(driver.find_element(by=By.ID, value=coin_id))

    
