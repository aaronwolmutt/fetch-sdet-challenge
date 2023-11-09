import os
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


@pytest.mark.skip
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


@pytest.mark.skip
def test_can_get_list_of_weights():
    """
        Requirement d, test that we can get a list of weights
    """
    
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    # fill left and right 0th position with 0 and 1
    driver.find_element(by=By.ID, value="left_0").send_keys("0")
    driver.find_element(by=By.ID, value="right_0").send_keys("1")

    # click on weigh
    driver.find_element(by=By.ID, value="weigh").click()

    # fill left and right 1th position with 2 and 3
    driver.find_element(by=By.ID, value="left_1").send_keys("2")
    driver.find_element(by=By.ID, value="right_1").send_keys("3")

    # click on weigh
    driver.find_element(by=By.ID, value="weigh").click()
    
    # search for the ordered list in game info
    driver.find_element(by=By.CLASS_NAME, value="game-info").find_elements(by=By.TAG_NAME, value="ol")


def test_gold_bar_alert_is_present():
    """
        Requirement e, check if clicking a gold bar sends an alert
    """
    
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    # click on the 0th gold bar
    driver.find_element(by=By.ID, value="coin_0").click()
    
    # fail the test if an alert is not present
    assert WebDriverWait(driver, 30).until(EC.alert_is_present())