import time

from scripts.init_browser import init_browser
from scripts.exceptions.driver_exception import DriverIsNoneException
from scripts.webdriver_functions import *

from selenium.webdriver.common.by import By

def main():
    print('I am running!')

    try:
        driver = init_browser()
    except DriverIsNoneException as de:
        print(de)
        
        return

    driver.get('https://bevasarlas.tesco.hu/groceries/hu-HU')

    html_ = driver.page_source

    # with open('asd.txt', 'w') as f:
    #     f.write(html_)

    menu_ul = wait_until_found(driver, 'menu-superdepartment', By.CLASS_NAME, 20)
    # categories = wait_until_found(driver, 'div.menu-tree__inner > ul', 30)
    # categories = menu_ul.find_elements_by_tag_name('li')
    categories = menu_ul.find_elements(By.TAG_NAME, 'li')
    for cat in categories:
        category = cat.text.replace('Vásárlás', '')
        category = category.replace('osztály', '')
        category = category.strip('\n')
        print(category)

    driver.close()

    return
