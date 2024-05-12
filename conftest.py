import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        'platformName': 'Android',
        "deviceName": "5200814efe0e35db",
        "appPackage": "xxxxxxxxxx",
        "appActivity": "com.xxxxxxx.xxxx.MainActivity",
        "automationName": "UiAutomator2",
        "noReset": True
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def stop_when_element_appears(driver):
    """
    Wait for the specified element to become visible on the screen.

    Args:
        driver: The WebDriver instance.
        timeout (int): The maximum time in seconds to wait for the element (default: 10).

    Returns:
        float: The time taken to reach the element.
    """
    scroll_view_locator = (MobileBy.ACCESSIBILITY_ID, "search_bar_textfield")
    start_time = time.time()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(scroll_view_locator))
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to reach the element: {time_taken} seconds")

    yield
