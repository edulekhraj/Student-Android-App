import time

from appium.webdriver.common.appiumby import AppiumBy

from Utilities.scroll_util import ScrollUtil


class UserHome:

    def __init__(self, driver):
        self.driver = driver

    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    live_classes_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="LIVE CLASSES"]'
    revision_list_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="REVISION LISTS"]'
    my_timeline_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="MY TIMELINE"]'
    my_home_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="MY HOME"]'
    home_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_home'
    my_favourite_books = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="My Favourite Books"]'
    live_classes_for_7_days_carousel = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Live Classes for the next 7 days"]'
    RL_topics_to_revise = AppiumBy.XPATH, '//android.widget.TextView[@text="Topics to revise"]'
    manage_books = AppiumBy.ID, 'com.embibe.student:id/favouriteBooksIcon'
    select_book = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/video_banner_card_view"])[1]'
    add_book_btn = AppiumBy.ID, 'com.embibe.student:id/txt_done'
    click_fav_book = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/video_banner_card_view"])[1]'
    the_embibe_big_books = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="The Embibe Big Books"]'
    embibe_big_books = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/video_banner_card_view"])[4]'
    test_i_have_taken = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="Tests I have taken"]'
    click_test_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/testBannerCardView"])[1]'
    view_test_fb_btn = AppiumBy.ID, 'com.embibe.student:id/btnTakeTest'
    test_fb_achieve_btn = AppiumBy.ID, 'com.embibe.student:id/tv_achieve'
    my_bookmark_carousel = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="My Bookmarks"]'
    videos_bookmark_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/container"])[1]'
    question_bookmark_tile =AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/container"])[2]'
    play_all_btn = AppiumBy.ID, 'com.embibe.student:id/btn_play_all'

    # def UH_module_click(self):
    #     self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
    #     self.driver.find_element(*UserHome.home_tab).click()
    #     time.sleep(5)
    #     self.driver.find_element(*UserHome.my_home_btn).click()
    #     time.sleep(3)
    #     ScrollUtil.swipeUp(1, self.driver)
    #     self.driver.find_element(*UserHome.live_classes_btn).click()
    #     time.sleep(3)
    #     # ScrollUtil.swipeUp(1, self.driver)
    #     # ScrollUtil.swipeUp(0.5, self.driver)
    #     ScrollUtil.swipeLeft(1,self.driver)
    #     self.driver.find_element(*UserHome.revision_list_btn).click()
    #     time.sleep(3)
    #     # ScrollUtil.swipeUp(1, self.driver)
    #     ScrollUtil.swipeLeft(1, self.driver)
    #     self.driver.find_element(*UserHome.my_timeline_btn).click()
    #     time.sleep(3)
    #     ScrollUtil.swipeUp(1, self.driver)
    #     time.sleep(3)

    def UH_add_fav_books(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver,UserHome.the_embibe_big_books)
        time.sleep(5)
        self.driver.find_element(*UserHome.manage_books).click()
        self.driver.find_element(*UserHome.add_book_btn).click()
        time.sleep(5)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.manage_books)
        self.driver.find_element(*UserHome.click_fav_book).click()

    def UH_Test_i_have_taken(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        try:
            ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.test_i_have_taken)
            time.sleep(5)
            self.driver.find_element(*UserHome.click_test_tile).click()
            self.driver.find_element(*UserHome.view_test_fb_btn).click()
            time.sleep(5)
            self.driver.find_element(*UserHome.test_fb_achieve_btn).click()
        except:
            print("No tests taken yet")


    def UH_embibe_big_books(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        time.sleep(3)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.the_embibe_big_books)
        ScrollUtil.swipeUp(1, self.driver)
        self.driver.find_element(*UserHome.embibe_big_books).click()
        time.sleep(3)


    def UH_bookmark_videos(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        time.sleep(3)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.videos_bookmark_tile)
        self.driver.find_element(*UserHome.videos_bookmark_tile).click()
        time.sleep(5)
        self.driver.find_element(*UserHome.play_all_btn).click()
        time.sleep(5)


    def UH_bookmark_questions(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.question_bookmark_tile)
        time.sleep(3)
        ScrollUtil.swipeUp(1, self.driver)
        self.driver.find_element(*UserHome.question_bookmark_tile).click()
        time.sleep(5)
        self.driver.find_element(*UserHome.play_all_btn).click()
        time.sleep(5)
