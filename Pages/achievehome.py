import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.practicehome import PracticeHome
from Pages.testhome import TestHome
from Utilities.scroll_util import ScrollUtil


class achieve_home:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    achieve_module = (AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Achieve']")
    start_achieving_btn = (
    AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/cv_enter_achieve"]')
    create_achieve_journey_btn = (
    AppiumBy.XPATH, '(//android.widget.TextView[@text="Create your new Achieve Journey"])[2]')
    first_sub = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[1]')
    first_chapt = (
    AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.embibe.student:id/cl_chapter_row_root'])[2]")
    second_chapt = (
        AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.embibe.student:id/cl_chapter_row_root'])[3]")
    continue_btn = (AppiumBy.XPATH, "//*[@text='Continue']")
    start_DT_1_btn = (AppiumBy.XPATH, "//*[contains(@text, 'Start')]")
    dt1_resume_test_btn = (AppiumBy.XPATH, "//*[@text='Resume']")
    test_submit_button = (AppiumBy.XPATH, "//*[contains(@text, 'Submit')]")
    dt1_view_feedback = (
    AppiumBy.ID, "com.embibe.student:id/btnContinueTest")
    start_dt2_test_from_feedback = (AppiumBy.ID, 'com.embibe.student:id/tv_achieve')
    plan_your_target = (AppiumBy.ID, 'com.embibe.student:id/btn_plan_for_your_target')
    target_score = (
    AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/cv_target2"])[2]')
    target_date = (AppiumBy.ID, 'com.embibe.student:id/llLayoutDate')
    target_date_next_month = (AppiumBy.ID, 'android:id/next')
    target_date_selection = (AppiumBy.XPATH, '//*[@text="24"]')
    journey_name = (AppiumBy.XPATH,
                    '//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/nameCard"]/android.widget.FrameLayout')
    generate_PAJ_btn = (AppiumBy.ID, 'com.embibe.student:id/tvGenerateStep3')
    congratulation_start_journey_btn = (AppiumBy.ID, 'com.embibe.student:id/tvButton')
    start_PAJ_journey = (AppiumBy.XPATH, "//*[@text='Start']")
    resume_PAJ_journey = (AppiumBy.XPATH, "//*[@text='Resume']")
    paj_skip_button = (AppiumBy.XPATH, "//*[@text='Skip']")
    i_will_take_test_later = (AppiumBy.XPATH, "//*[@text='I will take the test later']")
    explore_mastery = (AppiumBy.XPATH, "//*[@text='Explore Mastery']")
    explore_mastery_1st_chapter = (AppiumBy.XPATH,
                                   '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/rvExploreMastery"]/android.widget.LinearLayout[1]')
    explore_mastery_1st_topic = (
        AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.embibe.student:id/cvBgCard'])[2]")
    explore_mastery_1st_video = (AppiumBy.XPATH,
                                 '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[1]/android.view.ViewGroup')
    # dt2_start_test_btn =
    instruction_checkbox = (AppiumBy.ID, 'com.embibe.student:id/iv_checkbox')
    start_now_button = (AppiumBy.XPATH, "//*[@text='Start Now']")
    achieve_home_PAJ_tile = (AppiumBy.XPATH, "//*[contains(@text, 'Continue Part')]")

    def wait_for_visibility(self, locator):
        """Wait until an element is visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """Wait until an element is clickable and return it."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def create_diagnostic_test(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        try:
            self.wait_for_clickable(achieve_home.start_achieving_btn).click()
            self.wait_for_clickable(achieve_home.create_achieve_journey_btn).click()
        except:
            ScrollUtil.scroll_until_element_is_visible(self.driver, achieve_home.create_achieve_journey_btn)
            self.wait_for_clickable(achieve_home.create_achieve_journey_btn).click()
        time.sleep(5)
        self.wait_for_clickable(achieve_home.first_sub).click()
        self.wait_for_clickable(achieve_home.first_chapt).click()
        self.wait_for_clickable(achieve_home.second_chapt).click()
        time.sleep(2)
        self.wait_for_clickable(achieve_home.continue_btn).click()
        self.wait_for_visibility(achieve_home.start_DT_1_btn).is_displayed()
        time.sleep(5)

    def start_diagnostic_test1(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, achieve_home.dt1_resume_test_btn)
        self.wait_for_clickable(achieve_home.dt1_resume_test_btn).click()
        try:
            self.driver.find_element(AppiumBy.ID, "com.embibe.student:id/tvBtnStartTest").click()
        except NoSuchElementException:
            self.driver.find_element(AppiumBy.ID, "com.embibe.student:id/tvDiagnosticButton").click()

        try:
            self.wait_for_clickable(achieve_home.instruction_checkbox).click()
            self.wait_for_clickable(achieve_home.start_now_button).click()
            time.sleep(3)

        except:
            print("User resumes the test")

        # self.attempt_dt_test()
        self.wait_for_clickable(achieve_home.test_submit_button).click()
        self.wait_for_clickable(achieve_home.test_submit_button).click()
        time.sleep(2)
        self.wait_for_clickable(achieve_home.dt1_view_feedback).click()
        time.sleep(5)
        self.wait_for_clickable(achieve_home.start_dt2_test_from_feedback).is_displayed()

    def i_will_start_test_later(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        try:
            self.wait_for_clickable(achieve_home.start_achieving_btn).click()
            self.wait_for_clickable(achieve_home.create_achieve_journey_btn).click()
        except:
            ScrollUtil.scroll_until_element_is_visible(self.driver, achieve_home.create_achieve_journey_btn)
            self.wait_for_clickable(achieve_home.create_achieve_journey_btn).click()
        time.sleep(5)
        self.wait_for_clickable(achieve_home.first_sub).click()
        self.wait_for_clickable(achieve_home.first_chapt).click()
        self.wait_for_clickable(achieve_home.continue_btn).click()
        self.wait_for_visibility(achieve_home.start_DT_1_btn).is_displayed()
        self.wait_for_visibility(achieve_home.i_will_take_test_later).click()

    def explore_mastery_tile(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        self.wait_for_clickable(achieve_home.explore_mastery).click()
        time.sleep(5)

        self.wait_for_clickable(achieve_home.explore_mastery_1st_chapter).click()
        time.sleep(5)
        self.wait_for_clickable(achieve_home.explore_mastery_1st_topic).click()
        time.sleep(5)
        self.wait_for_clickable(achieve_home.explore_mastery_1st_video).click()
        time.sleep(5)

    def start_diagnostic_test2(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, achieve_home.dt1_resume_test_btn)
        self.wait_for_clickable(achieve_home.dt1_resume_test_btn).click()
        try:
            if self.driver.find_element(By.XPATH,
                                        '//android.widget.TextView[@resource-id="com.embibe.student:id/tvDiagnosticButton"]').text == "Start":

                self.driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@resource-id="com.embibe.student:id/tvDiagnosticButton"]').click()
                self.wait_for_clickable(achieve_home.instruction_checkbox).click()
                self.wait_for_clickable(achieve_home.start_now_button).click()
            elif self.driver.find_element(By.XPATH,
                                          '//android.widget.TextView[@resource-id="com.embibe.student:id/tvDiagnosticButton"]').text == "Resume":
                self.driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@resource-id="com.embibe.student:id/tvDiagnosticButton"]').click()
                time.sleep(5)

            else:
                self.driver.find_element(By.XPATH,
                                         '//android.widget.TextView[@resource-id="com.embibe.student:id/tvDiagnosticButton"]').click()
            self.wait_for_clickable(achieve_home.test_submit_button).click()
            self.wait_for_clickable(achieve_home.test_submit_button).click()
            self.wait_for_clickable(achieve_home.achieve_home_PAJ_tile).is_displayed()


        except Exception as e:
            print(f"An error occurred: {e}")


    def create_PAJ_journey(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, achieve_home.dt1_resume_test_btn)
        self.wait_for_clickable(achieve_home.dt1_resume_test_btn).click()
        self.driver.find_element(By.XPATH,
                                 '//android.widget.TextView[@resource-id="com.embibe.student:id/tvDiagnosticButton"]').click()
        self.wait_for_clickable(achieve_home.target_score).click()
        ScrollUtil.swipeUp(1, self.driver)
        self.wait_for_clickable(achieve_home.target_date).click()
        ScrollUtil.swipeUp(1, self.driver)
        self.wait_for_clickable(achieve_home.target_date_next_month).click()
        self.wait_for_clickable(achieve_home.target_date_selection).click()
        ScrollUtil.swipeUp(1, self.driver)
        # self.wait_for_clickable(achieve_home.journey_name).click()
        element = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.EditText[@resource-id="com.embibe.student:id/tv_journey_name"]')
        # element.set_value("Achieve Now")
        element.click()
        self.driver.hide_keyboard()
        element.send_keys("Achieve Now")
        self.wait_for_clickable(achieve_home.generate_PAJ_btn).click()
        self.wait_for_clickable(achieve_home.congratulation_start_journey_btn).click()
        self.wait_for_clickable(achieve_home.start_PAJ_journey).is_displayed()

    def start_PAJ(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *achieve_home.achieve_home_PAJ_tile)
        self.wait_for_clickable(achieve_home.achieve_home_PAJ_tile).click()

        try:
            self.wait_for_clickable(achieve_home.start_PAJ_journey).click()

        except Exception as e:
            self.wait_for_clickable(achieve_home.resume_PAJ_journey).click()

        try:
            skip_button = self.driver.find_element(*achieve_home.paj_skip_button)
            if skip_button.is_displayed():
                skip_button.click()
        except Exception as e:
            print("Skip button not found or not clickable:", e)

    def achieve_full_journey(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.wait_for_clickable(achieve_home.achieve_module).click()
        try:
            self.wait_for_clickable(achieve_home.start_achieving_btn).click()
            self.wait_for_clickable(achieve_home.create_achieve_journey_btn).click()
        except:
            ScrollUtil.scroll_until_element_is_visible(self.driver, achieve_home.create_achieve_journey_btn)
            self.wait_for_clickable(achieve_home.create_achieve_journey_btn).click()
        time.sleep(5)
        self.wait_for_clickable(achieve_home.first_sub).click()
        self.wait_for_clickable(achieve_home.first_chapt).click()
        self.wait_for_clickable(achieve_home.second_chapt).click()
        time.sleep(3)
        self.wait_for_clickable(achieve_home.continue_btn).click()
        self.wait_for_clickable(achieve_home.start_DT_1_btn).is_displayed()

        try:
            self.driver.find_element(AppiumBy.ID, "com.embibe.student:id/tvBtnStartTest").click()
        except NoSuchElementException:
            self.driver.find_element(AppiumBy.ID, "com.embibe.student:id/tvDiagnosticButton").click()

        self.wait_for_clickable(achieve_home.instruction_checkbox).click()
        self.wait_for_clickable(achieve_home.start_now_button).click()
        time.sleep(10)
        self.wait_for_clickable(achieve_home.test_submit_button).click()
        self.wait_for_clickable(achieve_home.test_submit_button).click()

        # self.attempt_dt_test()
        try:
            self.wait_for_clickable(achieve_home.dt1_view_feedback).click()
            time.sleep(5)
            self.wait_for_clickable(achieve_home.start_dt2_test_from_feedback).is_displayed()
            self.wait_for_clickable(achieve_home.start_dt2_test_from_feedback).click()
            self.wait_for_clickable(achieve_home.instruction_checkbox).click()
            self.wait_for_clickable(achieve_home.start_now_button).click()
            self.wait_for_clickable(achieve_home.test_submit_button).click()
            self.wait_for_clickable(achieve_home.test_submit_button).click()
            self.wait_for_clickable(achieve_home.plan_your_target).click()

        except:
            self.wait_for_clickable(achieve_home.plan_your_target).click()

        self.wait_for_clickable(achieve_home.target_score).click()
        ScrollUtil.swipeUp(1, self.driver)
        self.wait_for_clickable(achieve_home.target_date).click()
        ScrollUtil.swipeUp(1, self.driver)
        self.wait_for_clickable(achieve_home.target_date_next_month).click()
        self.wait_for_clickable(achieve_home.target_date_selection).click()
        ScrollUtil.swipeUp(1, self.driver)
        # self.wait_for_clickable(achieve_home.journey_name).click()
        element = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.EditText[@resource-id="com.embibe.student:id/tv_journey_name"]')
        # element.set_value("Achieve Now")
        element.click()
        self.driver.hide_keyboard()
        element.send_keys("Achieve Now")
        self.wait_for_clickable(achieve_home.generate_PAJ_btn).click()
        self.wait_for_clickable(achieve_home.congratulation_start_journey_btn).click()
        self.wait_for_clickable(achieve_home.start_PAJ_journey).is_displayed()
        self.wait_for_clickable(achieve_home.start_PAJ_journey).click()

    def extend_PAJ_journey(self):
        pass

    def attempt_dt_test(self):
        self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/iconList').click()
        ques_count = self.driver.find_elements(
            AppiumBy.XPATH,
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/recyclerQuestionSummary"]/android.view.ViewGroup'
        )
        print(f"Total Questions: {len(ques_count)}")
        time.sleep(2)

        self.driver.press_keycode(4)
        for k in range(1, len(ques_count) + 1):
            try:
                question = self.driver.find_element(
                    AppiumBy.XPATH,
                    '//android.widget.TextView[@resource-id="com.embibe.student:id/textQuestionType"]'
                ).text
            except NoSuchElementException:
                question = "Unknown"

            print(f"Question {k}: {question}")

            if question in ['   Single Choice', '   True False', '   Matrix Single Choice']:
                try:
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="A"]').click()
                except NoSuchElementException:
                    print("Option 'A' not found.")
                finally:
                    try:
                        self.driver.find_element(
                            AppiumBy.XPATH,
                            '//android.widget.TextView[@resource-id="com.embibe.student:id/btnSaveNext"]'
                        ).click()
                    except NoSuchElementException:
                        print("Save/Next button not found.")

            elif question == '   Multiple Choice':
                try:
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="A"]').click()
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="B"]').click()
                except NoSuchElementException:
                    print("Multiple Choice options not found.")
                finally:
                    try:
                        self.driver.find_element(
                            AppiumBy.XPATH,
                            '//android.widget.TextView[@resource-id="com.embibe.student:id/btnSaveNext"]'
                        ).click()
                    except NoSuchElementException:
                        print("Save/Next button not found.")

            elif question in ['   Subjective Numerical', '   Integer']:
                try:
                    input_field = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
                    input_field.click()
                    time.sleep(1)
                    input_field.send_keys("12")
                    self.driver.hide_keyboard()
                except NoSuchElementException:
                    print("Input field not found.")
                finally:
                    try:
                        self.driver.find_element(
                            AppiumBy.XPATH,
                            '//android.widget.TextView[@resource-id="com.embibe.student:id/btnSaveNext"]'
                        ).click()
                    except NoSuchElementException:
                        print("Save/Next button not found.")

            elif question == '   Multiple Fill In The Blanks':
                try:
                    for i in range(2):  # Assuming 2 blanks
                        blank_xpath = f'//android.view.View[@resource-id="fb-blank-{i}"]'
                        blank = self.driver.find_element(AppiumBy.XPATH, blank_xpath)
                        blank.click()
                        time.sleep(1)
                        blank.send_keys("FIB")
                        time.sleep(1)
                        self.driver.hide_keyboard()
                except NoSuchElementException:
                    print("Fill in the Blanks fields not found.")
                finally:
                    try:
                        self.driver.find_element(
                            AppiumBy.XPATH,
                            '//android.widget.TextView[@resource-id="com.embibe.student:id/btnSaveNext"]'
                        ).click()
                    except NoSuchElementException:
                        print("Save/Next button not found.")
            elif question == '   Fill In The Blanks':
                try:

                    blank_xpath = "//android.view.View[@resource-id='fb-blank-0']"
                    blank = self.driver.find_element(AppiumBy.XPATH, blank_xpath)
                    blank.click()
                    time.sleep(1)
                    blank.send_keys("FIB")
                    time.sleep(1)
                    self.driver.hide_keyboard()
                except NoSuchElementException:
                    print("Fill in the Blanks fields not found.")
                finally:
                    try:
                        self.driver.find_element(
                            AppiumBy.XPATH,
                            '//android.widget.TextView[@resource-id="com.embibe.student:id/btnSaveNext"]'
                        ).click()
                    except NoSuchElementException:
                        print("Save/Next button not found.")

            else:
                try:
                    self.driver.find_element(
                        AppiumBy.XPATH,
                        '//android.widget.TextView[@resource-id="com.embibe.student:id/btnSaveNext"]'
                    ).click()
                except NoSuchElementException:
                    print("Save/Next button not found.")
