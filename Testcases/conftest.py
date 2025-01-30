import allure
import appium
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

        # 'appium:ignoreHiddenApiPolicyError': True  # Corrected to use the string key
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


# @pytest.fixture()
# def log_on_failure(request, appium_driver):
#     yield
#     item = request.node
#     driver = appium_driver
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)



# def appiumdriver(request):
#     if request.param == 'device1':
#         desired_caps = dict(
#
#         deviceName = 'emulator-5554',
#         platformName = 'Android',
#         appActivity = 'com.embibe.jioembibe.mobile.LandingActivity',
#         appPackage = 'com.embibe.student',
#         automationName = 'UiAutomator2',
#         )
#         option=UiAutomator2Options().load_capabilities(desired_caps)
#         driver = webdriver.Remote("http://127.0.0.1:4723", options=option)
#
#     if request.param == 'device2':
#         desired_caps1 = dict(
#
#         deviceName = 'emulator-5556',
#         platformName = 'Android',
#         appActivity = 'com.embibe.jioembibe.mobile.LandingActivity',
#         appPackage = 'com.embibe.student',
#         automationName = 'UiAutomator2',
#         )
#         option=UiAutomator2Options().load_capabilities(desired_caps1)
#         driver = webdriver.Remote("http://127.0.0.1:4724", options=option)