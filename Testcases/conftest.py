import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
@pytest.fixture
def appiumdriver(request):
    desired_caps = {
        'deviceName': 'Android',
        'platformName': 'Android',
        'appActivity': 'com.embibe.jioembibe.mobile.LandingActivity',
        'appPackage': 'com.embibe.student',
        'automationName': 'UiAutomator2',
         'udid' : '100ba177',
         'ignoreHiddenApiPolicyError' : True,  # Corrected to use the string key
        'autoGrantPermissions': True

    }
    global driver
    option=UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=option)
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield driver
    driver.quit()



@pytest.yield_fixture
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failedtestcase", attachment_type= AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, appiumdriver):
    yield
    item = request.node
    driver = appiumdriver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)

# @pytest.fixture(params= ["device1", "device2"])
# def appiumdriver(request):
#
#     if request.param == "device1":
#         desired_caps = {
#             "deviceName": "Android",
#             "platformName": "Android",
#             "udid": "100ba177",
#             'appActivity': 'com.embibe.jioembibe.mobile.LandingActivity',
#             'appPackage': 'com.embibe.student',
#             "automationName": "UIAutomator2",
#             "noReset": True
#
#         }
#         options = UiAutomator2Options().load_capabilities(desired_caps)
#         driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#     if request.param == 'device2':
#             desired_caps = {
#                 "deviceName": "Android",
#                 "platformName": "Android",
#                 "udid": "RZ8N719WLCP",
#                 "appActivity": "com.embibe.jioembibe.mobile.LandingActivity",
#                 "appPackage": "com.embibe.student",
#                 "automationName": "UIAutomator2",
#                 "noReset": True
#
#             }
#             options = UiAutomator2Options().load_capabilities(desired_caps)
#             driver = webdriver.Remote("http://127.0.0.1:4725", options=options)
#         # options = UiAutomator2Options().load_capabilities(desired_caps)
#         # driver = webdriver.Remote("http://127.0.0.1/4723", options=options)
#     driver.get_screenshot_as_file("abc.png")
#     driver.get_device_time()
#     time.sleep(10)



