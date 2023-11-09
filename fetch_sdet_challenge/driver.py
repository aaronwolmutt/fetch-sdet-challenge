import logging
import os
from selenium import webdriver


def get_page():
    url = os.getenv("POETRY_CHALLENGE_URL")    
    driver = webdriver.Chrome()
    try:
        logging.info("Getting the challenge page")
        page = driver.get(url)
        return page
    except Exception as e:
        logging.error("Couldn't get the challenge page")
        raise ConnectionError()
