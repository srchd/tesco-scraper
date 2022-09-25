import os

from .os_and_browser_selector import select_web_browser
from .exceptions.browser_exception import BrowserNotFoundException
from .exceptions.driver_exception import DriverIsNoneException

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def init_browser():
    if 'edge' in select_web_browser().lower():
        browser_options = EdgeOptions()
        browser_options.use_chromium = True
    elif 'firefox' in select_web_browser().lower():
        browser_options = FireFoxOptions()
    else:
        raise BrowserNotFoundException('[Error] Invalid Browser!')

    browser_options.add_argument('--ignore-certificate-errors')
    browser_options.add_argument('--ignore-ssl-errors')
    browser_options.add_argument('--use-fake-ui-for-media-stream')
    # browser_options.add_experimental_option('prefs', {
    #     'credentials_enable_service': False,
    #     'profile.default_content_setting_values.media_stream_mic': 1,
    #     'profile.default_content_setting_values.media_stream_camera': 1,
    #     'profile.default_content_setting_values.geolocation': 1,
    #     'profile.default_content_setting_values.notifications': 1,
    #     'profile': {
    #         'password_manager_enabled': False
    #     }
    # })
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--no-first-run')

    # browser_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # browser_options.add_argument('--headless')
    browser_options.add_argument('--disable')

    driver = None
    if 'edge' in select_web_browser().lower():
        driver = Edge(EdgeChromiumDriverManager().install(), options=browser_options)
    elif 'firefox' in select_web_browser().lower():
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=browser_options)
    else:
        raise BrowserNotFoundException('[Error] Invalid Browser!')

    window_size = driver.get_window_size()
    if window_size['width'] < 1200:
        print("Resized window width")
        # logging.info("Resized window width")
        driver.set_window_size(1200, window_size['height'])

    if window_size['height'] < 850:
        print("Resized window height")
        # logging.info("Resized window height")
        driver.set_window_size(window_size['width'], 850)

    if not driver:
        raise DriverIsNoneException('[Error] Driver is None!')

    return driver