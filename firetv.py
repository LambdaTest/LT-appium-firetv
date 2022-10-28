from appium import webdriver
import os
from selenium.webdriver.common.by import By
import time

def getCaps():
    desired_caps = {
        "deviceName" : "Amazon Fire TV Stick",
        "platformVersion" :  "7",
        "platformName":"firetv",
        'isRealMobile':True,
        "build": "firetv",
        "video": True,
        #highlight-next-line
        "app":"APP_URL",      #Add app url here
        "network": True,
        "geoLocation": "FR",
        "devicelog": True,
    }

    return desired_caps

def runTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username below if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey below if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    # grid url
    gridUrl = "stage-mobile-hub-frankfurt.lambdatestinternal.com/wd/hub"

    # capabilities
    desired_cap = getCaps()
    url = "http://"+username+":"+accesskey+"@"+gridUrl

    print("Initiating remote driver on platform: "+desired_cap["deviceName"]+" browser: "+" version: "+desired_cap["platformVersion"])
    driver = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor= url
    )

    # run test
    print(driver.session_id)

    time.sleep(10)
    
    inputfield = driver.find_element(by = By.ID, value ="webpage")
    inputfield.click()

    inputfield = driver.find_element(by = By.ID, value = "websiteName")
    inputfield.send_keys("https://ifconfig.me")

    inputfield = driver.find_element(by = By.ID, value ="findButton")
    inputfield.click()

    time.sleep(3)
    list2 = driver.find_element(by= By.XPATH, value="//*[@resource-id='ip_address_cell']")
    print(list2.text)

    time.sleep(10)

    driver.execute_script("lambda-status=passed")

    driver.quit()

if __name__ == "__main__":
    runTest()
