import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from Pages.testhome import TestHome
from Utilities.scroll_util import ScrollUtil
from selenium.webdriver.support import expected_conditions as EC


class LearnHome(TestHome):

    def __init__(self, driver):
        self.driver = driver

    continue_learning_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Continue Learning"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    guided_tour_next_btn = AppiumBy.ID, 'com.embibe.student:id/tvNext'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    home_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_home'
    practice_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_practice'
    test_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_test'
    achieve_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_achieve'
    learn_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_learn'
    trending_videos_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Trending Videos for Your Exam"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    bookmark_button = AppiumBy.ID, 'com.embibe.student:id/bookmark'
    download_button = AppiumBy.ID, 'com.embibe.student:id/fl_download_container'
    video_close_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    video_resume_button = AppiumBy.ID, 'com.embibe.student:id/btn_resume'
    video_play_button = AppiumBy.ID, 'com.embibe.student:id/ivSummaryHeroBannerPlay1'
    more_topic_tile = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[2]'
    related_video_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[4]'
    embibe_explainer_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Embibe Explainers"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    books_tile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Books With Videos & Solutions"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
    add_book_button = AppiumBy.ID, 'com.embibe.student:id/btn_myBooks'
    book_chapter_button = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]'
    book_topic_button = AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.embibe.student:id/ll_topic"])[1]'
    book_practice_chapter_tile = AppiumBy.ID, 'com.embibe.student:id/thumbPracticeForChapterIV'
    book_practice_topic_tile = AppiumBy.ID, 'com.embibe.student:id/thumbPracticeForChapterIV'
    practice_quit_button = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    learn_chapter_tile = AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.embibe.student:id/header\" and contains(@text, 'Chapters From')]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]"
    learn_button = AppiumBy.ID, 'com.embibe.student:id/tvSummaryLearnButton'
    sincerity_score_tile = AppiumBy.ID, 'com.embibe.student:id/ivSincerityScorePlay'
    sincerity_score_close_btn = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    learn_PTR = AppiumBy.ID, 'com.embibe.student:id/clFullTileCheatSheet'
    topics_in_this_chapter = AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.embibe.student:id/llTile"])[1]'
    embibe_explainers = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[3]'
    prerequisite_topics_carousel = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Prerequisite Topics to Ace this Topic"]'
    prerequisite_topics_videos = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Prerequisite Topics to Ace this Topic"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/(//android.widget.LinearLayout[@resource-id="com.embibe.student:id/llTile"])[1]'
    chapterone = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/clBookChapter"])[1]'
    practice_on_this_carousel = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Practice on this chapter"]'
    practice_tile_click = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/thumbPracticeForChapterIV"])[1]'
    test_on_this_chapter = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Tests on this chapter"]'
    test_tile_click = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/testBannerCardView"])[1]'
    deny_mic_access = AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"
    def guided_tour(self):
        for i in range(1, 6):
            self.driver.find_element(*LearnHome.guided_tour_next_btn).click()

    def module_click(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*LearnHome.home_tab).click()
        home_car = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/headingSectionParentView"]').text
        home_car == 'Assignment from My Parents'
        time.sleep(3)

        self.driver.find_element(*LearnHome.practice_tab).click()
        # prac_car = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/headingSectionParentView"])[3]').text
        # time.sleep(3)
        # assert 'Adaptive Practice' in prac_car

        self.driver.find_element(*LearnHome.test_tab).click()
        time.sleep(3)

        self.driver.find_element(*LearnHome.achieve_tab).click()
        time.sleep(3)
        self.driver.find_element(*LearnHome.learn_tab).click()
        time.sleep(3)
        learn_car = self.driver.find_element(AppiumBy.XPATH,
                                             '(//android.widget.RelativeLayout[@resource-id="com.embibe.student:id/headingSectionParentView"])[2]').text
        'Live Class' in learn_car

    def trending_videos(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.trending_videos_tile)
        self.driver.find_element(*LearnHome.trending_videos_tile).click()
        self.video_details()

    def trending_videos_more_topic_videos_click(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.trending_videos_tile)
        time.sleep(2)
        self.driver.find_element(*LearnHome.trending_videos_tile).click()
        self.driver.find_element(*LearnHome.more_topic_tile).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()

    def trending_videos_related_video_click(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.trending_videos_tile)
        self.driver.find_element(*LearnHome.trending_videos_tile).click()
        time.sleep(2)
        self.driver.find_element(*LearnHome.related_video_tile).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()

    def embibe_explainer_videos(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.embibe_explainer_tile)
        self.driver.find_element(*LearnHome.embibe_explainer_tile).click()
        self.video_details()

    def embibe_explainers_more_topic_videos_click(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.trending_videos_tile)
        time.sleep(2)
        self.driver.find_element(*LearnHome.trending_videos_tile).click()
        self.driver.find_element(*LearnHome.more_topic_tile).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()

    def embibe_explainers_related_video_click(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(3)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.trending_videos_tile)
        self.driver.find_element(*LearnHome.trending_videos_tile).click()
        time.sleep(2)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.related_video_tile)
        self.driver.find_element(*LearnHome.related_video_tile).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()


    def books_with_videos_solutions(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.books_tile)
        self.driver.find_element(*LearnHome.books_tile).click()
        self.driver.find_element(*LearnHome.chapterone).click()
        self.driver.find_element(*LearnHome.chapterone).click()
        self.driver.find_element(AppiumBy.XPATH,
                                 '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/adBannerCardView"])[1]').click()
        time.sleep(5)
        time.sleep(2)
        try:
            if self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_resume').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(5)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()

    def learn_chapters(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        self.driver.find_element(*LearnHome.learn_button).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)

        # PTR

    def learn_ptr(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        self.driver.find_element(*LearnHome.learn_PTR).click()
        time.sleep(5)
        self.driver.press_keycode(4)

    def learn_sincerity_score(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        self.driver.find_element(*LearnHome.sincerity_score_tile).click()
        time.sleep(3)
        self.driver.press_keycode(4)
        self.driver.find_element(*LearnHome.sincerity_score_close_btn).click()
        time.sleep(3)

        ScrollUtil.swipeUp(1, self.driver)

    def learn_embibe_explainers(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *LearnHome.embibe_explainers)
        self.driver.find_element(*LearnHome.embibe_explainers).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
                time.sleep(3)
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)

    def learn_topics_in_this_chapter(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *LearnHome.topics_in_this_chapter)
        self.driver.find_element(*LearnHome.topics_in_this_chapter).click()

        self.driver.find_element(*LearnHome.learn_button).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)
        self.driver.press_keycode(4)

    def learn_prerequisite_topics(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *LearnHome.prerequisite_topics_carousel)
        time.sleep(2)
        self.driver.find_element(*LearnHome.prerequisite_topics_videos).click()
        time.sleep(3)
        self.driver.find_element(*LearnHome.learn_button).click()
        try:
            if self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()
            time.sleep(3)
        self.driver.press_keycode(4)

    def test_taking_in_learn_chapter(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, *LearnHome.test_on_this_chapter)
        time.sleep(2)
        self.driver.find_element(*LearnHome.test_tile_click).click()
        time.sleep(10)
        self.test_taking()

        self.driver.press_keycode(4)

    def practice_taking_in_chapter(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.learn_chapter_tile)
        time.sleep(5)
        self.driver.find_element(*LearnHome.learn_chapter_tile).click()

        ScrollUtil.scroll_until_element_is_visible(self.driver, *LearnHome.practice_on_this_carousel)
        time.sleep(2)
        self.driver.find_element(*LearnHome.practice_tile_click).click()
        time.sleep(10)
        self.practice_taking()

    def continue_learning(self):
        self.driver.find_element(*LearnHome.guided_tour_cancel_btn).click()
        time.sleep(5)
        # ScrollUtil.swipeUp(2, self.driver)
        # ScrollUtil.scrollToTextByAndroidUIAutomator('Continue Learning',self.driver)
        # self.driver.find_element(*LearnHome.continue_learning_tile).click()
        # self.video_details()

        ScrollUtil.scroll_until_element_is_visible(self.driver, LearnHome.continue_learning_tile)
        self.driver.find_element(*LearnHome.continue_learning_tile).click()
        self.video_details()

    def video_details(self):
        self.driver.find_element(*LearnHome.bookmark_button).click()
        # self.driver.find_element(*LearnHome.download_button).click()
        self.driver.find_element(*LearnHome.video_play_button).click()
        time.sleep(2)
        try:
            if self.driver.find_element(AppiumBy.ID, 'com.embibe.student:id/btn_resume').is_displayed():
                self.driver.find_element(*LearnHome.video_resume_button).click()
                time.sleep(5)
                self.driver.press_keycode(4)
                self.driver.find_element(*LearnHome.video_close_button).click()
        except NoSuchElementException:
            time.sleep(10)
            self.driver.press_keycode(4)
            self.driver.find_element(*LearnHome.video_close_button).click()



    def practice_taking(self):
        time.sleep(10)
        self.driver.find_element(*LearnHome.deny_mic_access).click()
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

    def test_taking(self):
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
