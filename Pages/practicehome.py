import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from Pages.learnhome import LearnHome
from Pages.testhome import TestHome

from Utilities.scroll_util import ScrollUtil


class PracticeHome(LearnHome, TestHome):

    def __init__(self, driver):
        self.driver = driver

    practice = (AppiumBy.ID, 'com.embibe.student:id/navigation_practice')
    practice_chapter = (AppiumBy.XPATH,
                        '//*[contains(@text, "Adaptive Practice Chapters From")]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    start_practice_btn = (AppiumBy.ID, 'com.embibe.student:id/tvSummaryLearnButton')
    bookmark_button = AppiumBy.XPATH, '//android.view.View[@resource-id="PracticeConatiner"]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[1]'
    guided_tour_cancel_btn = (AppiumBy.ID, 'com.embibe.student:id/ivClose')
    sincerity_score_tile = (AppiumBy.ID, 'com.embibe.student:id/ivSincerityScorePlay')
    attempt_quality_jar = (AppiumBy.ID, 'com.embibe.student:id/jar_recall')
    attempt_quality_jar_play = (
        AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.embibe.student:id/iv_play"]')
    practice_PTR = (AppiumBy.ID, 'com.embibe.student:id/clFullTileCheatSheet')
    topic_practice = (AppiumBy.XPATH,
                      '//*[contains(@text, "Topics for Practice")]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    recommended_learning = (AppiumBy.XPATH,
                            '//*[contains(@text, "Recommended")]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    more_tests = (AppiumBy.XPATH,
                  '//*[contains(@text, "Tests on this")]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')

    author_book = (AppiumBy.XPATH,
                   '//*[contains(@text, "Books With")]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    add_book_btn = (AppiumBy.ID, 'com.embibe.student:id/btn_myBooks')
    big_book = (AppiumBy.XPATH,
                '//*[contains(@text, "Embibe Big Books")]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    deny_mic_access = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']")
    def practice_chapter_tile(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        self.driver.find_element(*PracticeHome.start_practice_btn).click()
        self.practice_taking()

    def sincerity_score_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        self.driver.find_element(*PracticeHome.sincerity_score_tile).click()
        time.sleep(5)

    def attempt_quality_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        self.driver.find_element(*PracticeHome.attempt_quality_jar).click()
        self.driver.find_element(*PracticeHome.attempt_quality_jar_play).click()
        time.sleep(10)

    def PTR_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        self.driver.find_element(*PracticeHome.practice_PTR).click()
        time.sleep(5)
        ScrollUtil.swipeUp(2, self.driver)

    def topic_practice_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.topic_practice)
        self.driver.find_element(*PracticeHome.topic_practice).click()
        self.practice_taking()

    def recommended_learning_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.recommended_learning)
        self.driver.find_element(*PracticeHome.recommended_learning).click()
        time.sleep(5)
        self.video_details()

    def more_test_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.more_tests)
        self.driver.find_element(*PracticeHome.more_tests).click()
        self.test_taking()

    def author_book_in_practice_chapter(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.practice_chapter)
        self.driver.find_element(*PracticeHome.practice_chapter).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.author_book)
        self.driver.find_element(*PracticeHome.author_book).click()
        self.driver.find_element(*PracticeHome.add_book_btn).click()
        # self.driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.student:id/book_recycler_view"]/android.view.ViewGroup[1]').click()
        # self.driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]').click()
        # self.driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]').click()

    def embibe_author_book(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.author_book)
        # ScrollUtil.swipeUp(1, self.driver)
        self.driver.find_element(*PracticeHome.author_book).click()
        try :
            self.driver.find_element(*PracticeHome.add_book_btn).click()
        except :
            print("Book already added")

    def embibe_big_book(self):
        self.driver.find_element(*PracticeHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*PracticeHome.practice).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, PracticeHome.big_book)
        # ScrollUtil.swipeUp(1, self.driver)
        self.driver.find_element(*PracticeHome.big_book).click()
        time.sleep(5)

    def practice_taking(self):
        time.sleep(10)
        try:
            self.driver.find_element(*PracticeHome.deny_mic_access).click()
        except:
            pass

        for i in range(1, 4):
            self.driver.find_element(*PracticeHome.bookmark_button).click()
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
