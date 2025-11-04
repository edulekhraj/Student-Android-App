import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.scroll_util import ScrollUtil


class TestHome:

    def __init__(self, driver):
        self.driver = driver

    custom_test_tile = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/create_own_test"]'
    continue_btn = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_tab = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/navigation_bar_item_icon_container"])[4]'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    quick_5_min_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_quick_five_min_test'
    custom_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_name_field = AppiumBy.ID, 'com.embibe.student:id/et_test_name'
    create_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_create_test'
    test_btn = AppiumBy.ID, 'com.embibe.student:id/btnTakeTest'
    sel_new_embibe_expUI = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_env_popup = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_parent_close_video"]/android.view.ViewGroup'
    instruc_next_button = AppiumBy.ID, 'com.embibe.student:id/btn_next'
    instruct_chkbox = AppiumBy.ID, 'com.embibe.student:id/iv_checkbox'
    i_am_ready_to_begin_btn = AppiumBy.ID, 'com.embibe.student:id/btn_ready'
    old_test_ui_start_test_btn = AppiumBy.ID, 'com.embibe.student:id/btn_start'
    submit_btn = AppiumBy.XPATH, 'com.embibe.student:id/btnSubmitTest'
    submit_confirm_btn = AppiumBy.ID, 'com.embibe.student:id/btnSubmitTest'
    view_fb_btn = AppiumBy.ID, 'com.embibe.student:id/btnContinueTest'
    trending_test_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Trending Tests for Your Exam"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    full_test_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Take Full Tests"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    chapter_test_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Take Chapter Tests"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    recommended_learning_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Recommended Learning to Ace this Test"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    recommended_practice_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Recommended Practice to Ace this Test"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    more_tests = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="More Tests on this Syllabus"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
    video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    practice_milestone = AppiumBy.XPATH, '//android.widget.Image[@text="milestone-active"]'
    practice_close_btn = By.XPATH, '//android.widget.TextView[@text=""]'
    test_on_this_chapter = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="More Tests on this Syllabus"]'
    test_tile_click = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/testBannerCardView"])[1]'
    deny_mic_access = By.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"
    bookmark_button = By.XPATH, "//android.view.View[@resource-id='PracticeConatiner']/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.TextView"
    def five_mins_custom_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        ScrollUtil.scrollToTextByAndroidUIAutomator('My Custom Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.custom_test_tile)
        self.driver.find_element(*TestHome.custom_test_tile).click()
        sub_count = self.driver.find_elements(AppiumBy.XPATH,
                                              '//android.widget.GridView[@resource-id="com.embibe.student:id/rv_subjects"]/androidx.cardview.widget.CardView')
        print(len(sub_count))
        for i in range(1, len(sub_count) + 1):
            self.driver.find_element(AppiumBy.XPATH,
                                     '//android.widget.GridView[@resource-id="com.embibe.student:id/rv_subjects"]/androidx.cardview.widget.CardView[' + str(
                                         i) + ']').click()

        self.driver.find_element(*TestHome.continue_btn).click()
        time.sleep(3)

        for j in range(1, len(sub_count) + 1):
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[' + str(
                                         j) + ']').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_chapter_row_root"])[1]').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[' + str(
                                         j) + ']').click()
            # time.sleep(2)

        self.driver.find_element(*TestHome.quick_5_min_test_btn).click()
        time.sleep(10)
        self.test_taking()

        self.driver.press_keycode(4)

        # Recommended Learning to Ace this Test

    def custom_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        # ScrollUtil.scrollToTextByAndroidUIAutomator('My Custom Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.custom_test_tile)
        self.driver.find_element(*TestHome.custom_test_tile).click()
        sub_count = self.driver.find_elements(AppiumBy.XPATH,
                                              '//android.widget.GridView[@resource-id="com.embibe.student:id/rv_subjects"]/androidx.cardview.widget.CardView')
        print(len(sub_count))
        for i in range(1, len(sub_count) + 1):
            self.driver.find_element(AppiumBy.XPATH,
                                     '//android.widget.GridView[@resource-id="com.embibe.student:id/rv_subjects"]/androidx.cardview.widget.CardView[' + str(
                                         i) + ']').click()

        self.driver.find_element(*TestHome.continue_btn).click()
        time.sleep(3)

        for j in range(1, len(sub_count) + 1):
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[' + str(
                                         j) + ']').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_chapter_row_root"])[1]').click()
            # time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH,
                                     '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_subject_root"])[' + str(
                                         j) + ']').click()
            # time.sleep(2)

        self.driver.find_element(*TestHome.custom_test_btn).click()
        self.driver.find_element(*TestHome.test_name_field).send_keys('Custom Test')
        self.driver.find_element(*TestHome.create_test_btn).click()
        time.sleep(20)
        self.test_taking()

        self.driver.press_keycode(4)

    def trending_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Trending Tests for Your Exam', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.trending_test_tile)
        time.sleep(5)
        self.driver.find_element(*TestHome.trending_test_tile).click()
        self.test_taking()

        self.driver.press_keycode(4)

    def recommended_learning_to_ace_in_trending_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Full Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test

    def recommended_practice_to_ace_in_trending_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Full Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)
        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()

        # Test Taking in Chapter

    def more_test_taking_in_trending_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Full Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *TestHome.test_on_this_chapter)
        time.sleep(2)
        self.driver.find_element(*TestHome.test_tile_click).click()
        time.sleep(10)
        self.more_test_taking()
        self.driver.press_keycode(4)

    def full_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Full Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        self.test_taking()
        self.driver.press_keycode(4)

    def recommended_learning_to_ace_this_full_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test

    def recommended_practice_to_ace_this_full_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)
        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()

        # Test Taking in Chapter

    def more_test_taking_in_full_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.full_test_tile)
        self.driver.find_element(*TestHome.full_test_tile).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, *TestHome.test_on_this_chapter)
        time.sleep(2)
        self.driver.find_element(*TestHome.test_tile_click).click()
        time.sleep(10)
        self.more_test_taking()
        self.driver.press_keycode(4)

    def chapter_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Chapter Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.chapter_test_tile)

        self.driver.find_element(*TestHome.chapter_test_tile).click()
        self.test_taking()
        self.driver.press_keycode(4)

    def recommended_learning_to_ace_this_chapter_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Chapter Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.chapter_test_tile)

        self.driver.find_element(*TestHome.chapter_test_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_learning_tile)
        self.driver.find_element(*TestHome.recommended_learning_tile).click()
        time.sleep(3)
        self.video_details()

        # Recommended Practice to Ace this Test

    def recommended_practice_to_ace_this_chapter_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Chapter Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.chapter_test_tile)

        self.driver.find_element(*TestHome.chapter_test_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.recommended_practice_tile)
        self.driver.find_element(*TestHome.recommended_practice_tile).click()
        time.sleep(10)
        # self.driver.find_element(*TestHome.practice_milestone).is_displayed()
        self.practice_taking()

        # Test Taking in Chapter

    def more_test_taking_in_chapter_test(self):
        self.driver.find_element(*TestHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        self.driver.find_element(*TestHome.test_tab).click()
        time.sleep(5)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Take Chapter Tests', self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, TestHome.chapter_test_tile)

        self.driver.find_element(*TestHome.chapter_test_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *TestHome.test_on_this_chapter)
        time.sleep(2)
        self.driver.find_element(*TestHome.test_tile_click).click()
        time.sleep(10)
        self.more_test_taking()
        self.driver.press_keycode(4)

    def test_taking(self):
        try:
            btn = self.driver.find_element(*TestHome.test_btn).text

            if btn == 'Start Test':
                self.driver.find_element(*TestHome.test_btn).click()
                try:
                    popup_element = self.driver.find_element(*TestHome.test_env_popup)
                    if popup_element.is_displayed():
                        self.driver.find_element(*TestHome.sel_new_embibe_expUI).click()
                        self.driver.find_element(*TestHome.instruc_next_button).click()
                        self.driver.find_element(*TestHome.instruct_chkbox).click()
                        self.driver.find_element(*TestHome.i_am_ready_to_begin_btn).click()
                        self.take_test()
                except NoSuchElementException:
                    self.driver.find_element(*TestHome.instruct_chkbox).click()
                    self.driver.find_element(*TestHome.old_test_ui_start_test_btn).click()
                    time.sleep(10)
                    self.take_test()

            elif btn == 'Resume Test':
                self.driver.find_element(*TestHome.test_btn).click()
                time.sleep(10)
                self.take_test()

            self.driver.find_element(*TestHome.submit_btn).click()
            time.sleep(5)
            self.driver.find_element(*TestHome.submit_confirm_btn).click()
            time.sleep(5)
            self.driver.find_element(*TestHome.view_fb_btn).click()
            time.sleep(15)
            # assert "Predicted Improvement" == self.driver.find_element("//*[contains(text(),'Predicted')]").text

        except Exception as e:
            if btn == 'View Test Feedback':
                print("Test already Taken")
            elif btn == 'Expired':
                print("Test has been Expired")

    def more_test_taking(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            try:
                popup_displayed = self.driver.find_element(*TestHome.test_env_popup).is_displayed()
            except NoSuchElementException:
                popup_displayed = False  # If the popup is not found, assume it's not displayed

            if popup_displayed:
                print("Popup is displayed. Handling popup flow...")
                # Handle popup flow
                wait.until(EC.element_to_be_clickable(TestHome.sel_new_embibe_expUI)).click()
                wait.until(EC.element_to_be_clickable(TestHome.instruc_next_button)).click()
                wait.until(EC.element_to_be_clickable(TestHome.instruct_chkbox)).click()
                wait.until(EC.element_to_be_clickable(TestHome.i_am_ready_to_begin_btn)).click()
                time.sleep(10)
                self.take_test()
                wait.until(EC.element_to_be_clickable(TestHome.submit_btn)).click()
                wait.until(EC.element_to_be_clickable(TestHome.submit_confirm_btn)).click()
                wait.until(EC.element_to_be_clickable(TestHome.view_fb_btn)).click()

            else:
                wait.until(EC.element_to_be_clickable(TestHome.instruct_chkbox)).click()
                wait.until(EC.element_to_be_clickable(TestHome.old_test_ui_start_test_btn)).click()
                time.sleep(10)
                self.take_test()
                wait.until(EC.element_to_be_clickable(TestHome.submit_btn)).click()
                wait.until(EC.element_to_be_clickable(TestHome.submit_confirm_btn)).click()
                wait.until(EC.element_to_be_clickable(TestHome.view_fb_btn)).click()

        except:
            print("Test already taken")

    def video_details(self):
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*TestHome.video_resume_button).click()
                time.sleep(3)
                self.driver.press_keycode(4)
                self.driver.find_element(*TestHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(3)
            self.driver.press_keycode(4)
            self.driver.find_element(*TestHome.video_close_button).click()

    def practice_taking(self):
        time.sleep(10)
        try:
            self.driver.find_element(*TestHome.deny_mic_access).click()
        except:
            pass

        for i in range(1, 4):
            try:
                time.sleep(3)
                question_element = self.driver.find_element(AppiumBy.XPATH,
                                                            '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View/android.widget.TextView[1]').text
                print(question_element)
                self.driver.find_element(*TestHome.bookmark_button).click()

                if "Multiple Choice" in question_element:
                    time.sleep(5)

                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[3]').click()

                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[4]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Single Choice" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                             "//android.view.View[@resource-id=\"PracticeConatiner\"]/android.view.View[1]/android.view.View[4]").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "True-False" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[4]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Assertion" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[2]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Single DropDown" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Select\")").click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="Select"]/parent::android.view.View/parent::android.view.View/android.view.View[2]/android.view.View/android.widget.TextView[1]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Subjective" in question_element:
                    # self.driver.find_element(By.XPATH,
                    #                     "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()

                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Full Solution\")").click()
                    time.sleep(10)

                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Subjective Numerical" in question_element:
                    time.sleep(5)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Solve With Us\")").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Full Solution\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Subjective Answer" in question_element:
                    time.sleep(5)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Solve With Us\")").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             value="new UiSelector().text(\"Full Solution\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Fill in The Blanks" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@resource-id=\"fb-blank-0\"]").click()
                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="fb-blank-0"]/android.widget.EditText').send_keys(
                        "abc")
                    self.driver.hide_keyboard()
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Check"]').click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Integer" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                             "//div[@class='Title_title__og5qd']/div/div[2]/span/span/i").click()
                    self.driver.find_element(AppiumBy.CSS_SELECTOR, "[id='fb-blank-0']").click()
                    time.sleep(2)

                    self.driver.find_element(AppiumBy.CSS_SELECTOR, "[status='DEFAULT']").send_keys("1")
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Check']").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

                elif "Multiple Fill in The Blanks" in question_element:
                    self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="fb-blank-0"]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="fb-blank-0"]/android.widget.EditText').send_keys(
                        "abc")
                    self.driver.hide_keyboard()

                    self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="fb-blank-1"]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                             '//android.view.View[@resource-id="fb-blank-1"]/android.widget.EditText').send_keys(
                        "xyz")
                    self.driver.hide_keyboard()

                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Check']").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

                    # driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Solve With Us\"]").click()
                    # driver.find_element(AppiumBy.XPATH, "//*[@text='Full Solution']").click()
                    # driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

                elif "Learn Intervention" in question_element:
                    self.driver.find_element(AppiumBy.XPATH,
                                             "//android.widget.Button[@text=\"Continue Practice\"]").click()

            except NoSuchElementException:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Solve With Us\"]").click()
                self.driver.find_element(AppiumBy.XPATH, "//*[@text='Full Solution']").click()
                self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text=""]').click()
        self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_quit').click()

    def take_test(self):
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
