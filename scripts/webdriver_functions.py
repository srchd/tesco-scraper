from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions

def wait_until_found(driver, sel, by, timeout, expected_more=False, print_error=True):
    try:
        element_present = EC.visibility_of_element_located((by, sel))
        WebDriverWait(driver, timeout).until(element_present)

        return driver.find_element(by, sel) if not expected_more else driver.find_elements(by, sel)
    except exceptions.TimeoutException as e:
        if print_error:
            print(f'Timeout waiting for element: {sel}')
            print(f'\nERROR: {str(e)}')
            # logger.error(f'Timeout waiting for element: {sel}')
            # logger.error(f'\nERROR: {str(e)}')
        return None