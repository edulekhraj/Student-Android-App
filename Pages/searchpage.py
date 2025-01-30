import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.learnhome import LearnHome
from Pages.testhome import TestHome
from Utilities.configReader import readConfig


class Search_Module(TestHome):

    def __init__(self, driver):
        self.driver=driver

    keyword = readConfig('prod', 'search_kw')

    search_btn = AppiumBy.ID, 'com.embibe.student:id/search'
    search_field = AppiumBy.ID, 'com.embibe.student:id/query'
    result_tile = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[1]'
    learn_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Learn"]'
    books_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Books"]'
    questions_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Questions"]'
    questions_tile = AppiumBy.ID, 'com.embibe.student:id/questionCL'
    practice_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Practice"]'
    test_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Test"]'
    ptr_tab = AppiumBy.XPATH, '//android.widget.TextView[@text="Points to Remember"]'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    home_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_home'
    bookmark_button = AppiumBy.ID, 'com.embibe.student:id/bookmark'
    download_button = AppiumBy.ID, 'com.embibe.student:id/fl_download_container'
    video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
    change_goal_popup = AppiumBy.ID, 'com.embibe.student:id/do_u_want_view_TV'
    update_goal_btn = AppiumBy.ID, 'com.embibe.student:id/upgrade_goal_TV'
    practice_milestone = AppiumBy.XPATH, '//android.widget.Image[@text="milestone-active"]'
    book_chapter = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]'
    book_topic_video = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[1]'
    book_practice_tile = AppiumBy.ID , 'com.embibe.student:id/thumbPracticeForChapterIV'
    book_ptr_tile =  AppiumBy.ID, 'com.embibe.student:id/thumbCheatSheet'
    share_button = AppiumBy.ID, 'com.embibe.student:id/ivShare'
    test_env_popup = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_parent_close_video"]/android.view.ViewGroup'
    test_env_continue_btn = AppiumBy.ID, 'com.embibe.student:id/btn_continue'
    test_instru_next_btn = AppiumBy.ID, 'com.embibe.student:id/btn_next'
    test_instru_checkbox_btn = AppiumBy.ID, 'com.embibe.student:id/iv_checkbox'
    test_i_am_ready_to_begin_btn = AppiumBy.ID, 'com.embibe.student:id/btn_ready'
    test_old_ui_start_now_btn = AppiumBy.ID, 'com.embibe.student:id/btn_start'
    test_fb_achieve_btn = AppiumBy.ID, 'com.embibe.student:id/tv_continue_learning'
    practice_close_btn = By.XPATH, '//android.widget.TextView[@text=""]'
    deny_mic_access = By.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"

    def search_module_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        self.driver.find_element(*Search_Module.home_tab).click()
        time.sleep(5)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.learn_tab).click()
        self.driver.find_element(*Search_Module.books_tab).click()
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.questions_tab).click()
        self.driver.find_element(*Search_Module.test_tab).click()
        self.driver.find_element(*Search_Module.ptr_tab).click()

    def search_learn_video_click(self):

            self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
            time.sleep(10)
            self.driver.find_element(*Search_Module.search_btn).click()
            time.sleep(2)
            self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
            self.driver.press_keycode(66)
            self.driver.find_element(*Search_Module.learn_tab).click()
            self.driver.find_element(*Search_Module.result_tile).click()
            try:
                # Check if the goal change popup is displayed
                if self.driver.find_element(*Search_Module.change_goal_popup).is_displayed():
                    self.driver.find_element(*Search_Module.update_goal_btn).click()
            except:
                pass

            self.video_details()



    def search_practice_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(10)
        try:
            # Check if the exam change popup is displayed and click if found
            if self.driver.find_element(*Search_Module.change_goal_popup).is_displayed():
                self.driver.find_element(*Search_Module.update_goal_btn).click()
                time.sleep(10)  # Wait for the next element to appear

            # Check if the practice milestone is displayed
                self.driver.find_element(*Search_Module.practice_milestone).is_displayed()
                self.driver.press_keycode(66)

        except Exception as e:
            # Handle the exception and still check for the practice milestone
            time.sleep(10)
            self.practice_taking()

    def search_question_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.questions_tab).click()
        self.driver.find_element(*Search_Module.questions_tile).click()
        time.sleep(5)
        assert  self.driver.find_element(AppiumBy.XPATH, '//*[@text="Explanation:"]').is_displayed()

    def search_book_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.books_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        try:
        # Check if the goal change popup is displayed
            if self.driver.find_element(*Search_Module.change_goal_popup).is_displayed():
                self.driver.find_element(*Search_Module.update_goal_btn).click()
        except:
            print("no Goal Pop up Appeared")
        time.sleep(4)
        self.driver.find_element(*Search_Module.share_button).is_displayed()
        # self.driver.find_element(*LearnHome.chapterone).click()
        # self.driver.find_element(*LearnHome.chapterone).click()
        # self.driver.find_element(AppiumBy.XPATH,
        #                          '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[1]').click()
        #
        # self.video_details()

        #Chapter and Topic Click
        # time.sleep(5)
        # self.driver.find_element(*Search_Module.book_chapter).click()
        # self.driver.find_element(*Search_Module.book_practice_tile).click()
        # time.sleep(5)
        # self.driver.find_element(*Search_Module.practice_milestone).is_displayed()
        # self.driver.press_keycode(4)
        # self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_quit').click()
        # time.sleep(5)
        # self.driver.find_element(*Search_Module.book_ptr_tile).click()
        # self.driver.find_element(*Search_Module.book_chapter).click()
        # self.driver.find_element(*Search_Module.book_topic_video).click()
        # self.video_details()
        #

    def search_PTR_click(self):
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
        self.driver.press_keycode(66)
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.ptr_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(5)

    def search_test_and_click(self):
        # Cancel the guided tour if the button is displayed
        self.driver.find_element(*Search_Module.guided_tour_cancel_btn).click()
        time.sleep(10)

        # Perform search for "Current"
        self.driver.find_element(*Search_Module.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*Search_Module.search_field).send_keys(Search_Module.keyword)
        self.driver.press_keycode(66)

        # Navigate through tabs and select the result tile
        self.driver.find_element(*Search_Module.practice_tab).click()
        self.driver.find_element(*Search_Module.test_tab).click()
        self.driver.find_element(*Search_Module.result_tile).click()
        time.sleep(2)

        try:
        # Check if the goal change popup is displayed
            if self.driver.find_element(*Search_Module.change_goal_popup).is_displayed():
                self.driver.find_element(*Search_Module.update_goal_btn).click()
        except:
            print("no Goal Pop up Appeared")
        time.sleep(5)

        try:
            if self.driver.find_element(*Search_Module.test_env_popup).is_displayed():
                self.driver.find_element(*Search_Module.test_env_continue_btn).click()
                self.driver.find_element(*Search_Module.test_instru_next_btn).click()
                self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
                self.driver.find_element(*Search_Module.test_i_am_ready_to_begin_btn).click()
                time.sleep(10)
                self.take_test()
        except:
            print("no Goal Pop up Appeared")

        try:

            if self.driver.find_element(*Search_Module.test_instru_checkbox_btn).is_displayed():
                self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
                self.driver.find_element(*Search_Module.test_old_ui_start_now_btn).click()
                time.sleep(10)
                self.take_test()
        except:
            pass


        # Fallback: Check if the feedback achievement button is displayed
        else:
             print("Test already submitted")


    def video_details(self):
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*Search_Module.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*Search_Module.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*Search_Module.video_close_button).click()

    def practice_taking(self):
        time.sleep(10)
        self.driver.find_element(*Search_Module.deny_mic_access).click()
        for i in range(1, 4):
            try:
                time.sleep(3)
                question_element = self.driver.find_element(AppiumBy.XPATH,
                                                       '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View/android.widget.TextView[1]').text
                print(question_element)

                if "Multiple Choice" in question_element:
                    time.sleep(5)

                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[3]').click()

                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[4]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Single Choice" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        "//android.view.View[@resource-id=\"PracticeConatiner\"]/android.view.View[1]/android.view.View[4]").click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "True-False" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[4]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

                elif "Assertion" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[2]').click()
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
                    time.sleep(10)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()


                elif "Single DropDown" in question_element:
                    time.sleep(3)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Select\")").click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.TextView[@text="Select"]/parent::android.view.View/parent::android.view.View/android.view.View[2]/android.view.View/android.widget.TextView[1]').click()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Check\")").click()
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
                    self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Continue Practice\"]").click()

            except NoSuchElementException:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text=\"Solve With Us\"]").click()
                self.driver.find_element(AppiumBy.XPATH, "//*[@text='Full Solution']").click()
                self.driver.find_element(AppiumBy.XPATH, "//*[@text='Continue']").click()

        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text=""]').click()
        self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_quit').click()