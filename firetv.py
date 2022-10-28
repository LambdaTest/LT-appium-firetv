from xml.dom.expatbuilder import Rejecter
from appium import webdriver
from selenium.webdriver.common.by import By
import time


def getCaps():
    desired_cap= {
        "deviceName" : "Amazon Fire TV Stick",
        "platformVersion" :  "7",
        "platformName":"fireos",
        "isRealMobile":True,
        "build": "firetv",
        "video": True,
        "app":"APP_URL",  #Add app url here
        "network": True,
        "geoLocation": "RU",
        "devicelog": True,
        "visual":True
    }

    return desired_cap

def runTest():
    username = "YOUR_LAMBDATEST_USERNAME"           #Add your username here
    accessToken = "YOUR_LAMBDATEST_ACCESSKEY"       #Add your accessKey here

    gridUrl = "mobile-hub-internal.lambdatest.com/wd/hub"

    # capabilities
    desired_cap = getCaps()
    url = "http://"+username+":"+accessToken+"@"+gridUrl

    print("Initiating remote driver on platform: " +
          desired_cap["deviceName"]+" browser: "+" version: "+desired_cap["platformVersion"])

    start = time.time()
    driver = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor=url
    )

    # run test
    print(driver.session_id)
    time.sleep(10)

    inputfield = driver.find_element(by = By.ID, value ="enterText")
    inputfield.send_keys("https://ifconfig.me")

    time.sleep(2)

    inputfield = driver.find_element(by = By.ID, value ="JustAButton")
    inputfield.click()

    time.sleep(10)
    list2 = driver.find_element(by= By.XPATH, value="//*[@resource-id='ip_address_cell']")
    print(list2.text)

    time.sleep(50)

    driver.execute_script("lambda-status=passed")

    driver.quit()
    end = time.time()

    print("time taken: ", end - start)


if __name__ == "__main__":
    runTest()
