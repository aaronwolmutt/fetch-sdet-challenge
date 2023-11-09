import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.skip
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

@pytest.mark.skip
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


def test_can_type_nums_onto_grids():
    """
        Requirement c, test that numbers 0-8 can be typed onto the boards
    """
    
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    
    # fill the left
    for i in range(0, 9):
        driver.find_element(by=By.ID, value=f"left_{i}").send_keys(str(i))

    # fill the right
    for i in range(0, 9):
        driver.find_element(by=By.ID, value=f"right_{i}").send_keys(str(i))
