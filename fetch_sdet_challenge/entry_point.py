import logging

from fetch_sdet_challenge.driver import *

def main():
    page = get_page()
    print(type(page))