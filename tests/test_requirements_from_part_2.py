import os

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_clicks_on_buttons():
    """
        Requirement a, test that the weigh and reset buttons can be clicked
    """
    
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    # locate the weigh and reset buttons
    driver.find_element(by=By.ID, value="weigh").click()
    driver.find_element(by=By.ID, value="reset").click()


def test_get_measurement_field():
    """
        Requirement b, test that we can get the result field between the game boards

    """
    
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    # locate the result field
    driver.find_element(by=By.CLASS_NAME, value="result")
