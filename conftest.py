from appium import webdriver
from appium.options.common.base import AppiumOptions
from config.data import Data
import os
from urllib.parse import urlparse
import json
import http.client
import pytest

@pytest.fixture(scope="function")
def driver(request):
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "14",
        "appium:app": "app/app-release.apk",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def auth_user():

    host = os.getenv("HOST")
    part_host = urlparse(host).netloc
    conn = http.client.HTTPSConnection(part_host)
    payload = json.dumps({
        "email": Data.LOGIN,
        "password": Data.PASSWORD
    })
    headers = {'Content-Type': 'application/json'}
    conn.request("POST", "/api/user/login", payload, headers)
    res = conn.getresponse()
    response_data = res.read()
    response_data = json.loads(response_data.decode('utf-8'))

    user_data = json.dumps(response_data)
    token_id = response_data.get("tokenId")
    access_token = response_data.get("accessToken")
    user_email = response_data.get("email")

    return token_id, access_token



