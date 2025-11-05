
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
import time
from Pages.landingPages import landingpages
from Pages.searchpage import Search_Module
from Pages.testhome import TestHome
from Utilities.scroll_util import ScrollUtil


class UserHome(TestHome):

    def __init__(self, driver):
        self.driver = driver

    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    live_classes_btn = AppiumBy.XPATH, '//*[contains(@text,"RECORDED CLASSES")]'
    revision_list_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="REVISION LISTS"]'
    my_timeline_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="MY TIMELINE"]'
    my_home_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tvSubjectName" and @text="MY HOME"]'
    home_tab = AppiumBy.ID, 'com.embibe.student:id/navigation_home'
    my_favourite_books = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/header" and @text="My Favourite Books"]'
    past_class_carousel = AppiumBy.XPATH, '//*[contains(@text,"Past Classes")]'
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
    school_test_carousel = AppiumBy.XPATH, "//*[contains(@text,'Test from')]"
    school_test_carousel_1_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/fl_container"])[3]/android.view.ViewGroup[1]'
    assignment_card = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_custom_test_title"]'
    school_assignment_carousel = AppiumBy.XPATH,  "//*[contains(@text,'Assignment from')]"
    school_assignment_carousel_1_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/fl_container"])[1]/android.view.ViewGroup[1]'
    school_prerequisite_carousel = AppiumBy.XPATH, "//*[contains(@text,'Pre-Requisite Readiness Videos')]"
    school_prerequisite_carousel_1_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/fl_container"])[5]/android.view.ViewGroup[1]'
    school_recap_carousel = AppiumBy.XPATH, "//*[contains(@text,'Recap Videos from')]"
    school_recap_carousel_1_tile = AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.embibe.student:id/fl_container"])[5]/android.view.ViewGroup[1]'
    assignment_video_card = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[1]'

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

    def UH_recorded_classes(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        ScrollUtil.swipeUp(1, self.driver)
        self.driver.find_element(*UserHome.live_classes_btn).click()
        ScrollUtil.swipeUp(1, self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.past_class_carousel)

        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Past Classes"]/parent::android.widget.RelativeLayout/parent::android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[@text="Watch Now"]').click()
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="Watch Recording"]').click()
        time.sleep(5)

    def UH_revision_list(self):
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        My_Home = self.driver.find_element(AppiumBy.XPATH, "//*[@text='RECORDED CLASSES']")
        ScrollUtil.swipeUp(1, self.driver)

        # Get coordinates and size
        location =My_Home.location
        size = My_Home.size

        # Start from right side of element, end at left side
        start_x = location['x'] + size['width'] * 1
        start_y = location['y'] + size['height'] / 2
        end_x = location['x'] + size['width'] * 0.3

        # Define touch pointer
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")

        # Build the swipe action
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(end_x, start_y)
        actions.pointer_action.move_to_location(end_x, start_y)
        actions.pointer_action.pause(0.2)
        actions.pointer_action.release()

        # Perform the action
        actions.perform()

        self.driver.find_element(*UserHome.revision_list_btn).click()
        time.sleep(5)

    def UH_revision_list_questions(self):
        self.UH_revision_list()
        ScrollUtil.swipeUp(1, self.driver)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='IMPORTANT QUESTIONS']").click()
        time.sleep(2)

    def UH_revision_list_videos(self):
        self.UH_revision_list()
        ScrollUtil.swipeUp(1,self.driver)
        self.driver.find_element(*UserHome.RL_topics_to_revise).click()
        time.sleep(2)

    def school_cred(self):
        lp = landingpages(self.driver)
        lp.school_credential_login()

    def UH_School_Test_Assignment(self):
        self.school_cred()
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        time.sleep(5)
        ScrollUtil.swipeUp(1, self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.school_test_carousel)
        time.sleep(3)
        self.driver.find_element(*UserHome.school_test_carousel_1_tile).click()
        time.sleep(3)
        self.driver.find_element(*UserHome.assignment_card).click()
        self.test_env_selection()

    def UH_School_Recap_Videos_Assignment(self):
        self.school_cred()
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        time.sleep(5)
        ScrollUtil.swipeUp(1, self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver,UserHome.school_recap_carousel)
        time.sleep(2)
        self.driver.find_element(*UserHome.school_recap_carousel_1_tile).click()
        time.sleep(3)
        self.driver.find_element(*UserHome.assignment_video_card).click()
        self.video_details()

    def UH_School_Prerequisite_Videos_Assignment(self):
        self.school_cred()
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        time.sleep(5)
        ScrollUtil.swipeUp(1, self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.school_prerequisite_carousel)
        time.sleep(2)
        self.driver.find_element(*UserHome.school_prerequisite_carousel_1_tile).click()
        time.sleep(3)
        self.driver.find_element(*UserHome.assignment_video_card).click()
        self.video_details()

    def UH_School_Assignment_Assignment(self):
        self.school_cred()
        self.driver.find_element(*UserHome.guided_tour_cancel_btn).click()
        self.driver.find_element(*UserHome.home_tab).click()
        time.sleep(5)
        ScrollUtil.swipeUp(1, self.driver)
        ScrollUtil.scroll_until_element_is_visible(self.driver, UserHome.school_assignment_carousel)
        time.sleep(2)
        self.driver.find_element(*UserHome.school_assignment_carousel_1_tile).click()
        time.sleep(3)
        try:
            # Check for assigned video
            video = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Assigned Video']")
            if video.is_displayed():
                self.driver.find_element(AppiumBy.XPATH,
                                         '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[1]').click()
                self.video_details()

                # Ensure we’re back on home/assignment screen
                time.sleep(2)
        except Exception as e:
            print("No video assigned:", e)

        # Add small delay before checking next carousel
        time.sleep(2)

        try:
            # Check for assigned practice
            practice = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Assigned Practice']")
            if practice.is_displayed():
                self.driver.find_element(AppiumBy.XPATH,
                                         '(//android.widget.ImageView[@resource-id="com.embibe.student:id/imgBanner"])[2]').click()
                time.sleep(2)
                self.practice_taking()
        except Exception as e:
            print("No practice assigned:", e)


    def test_env_selection(self):
        try:
            if self.driver.find_element(*Search_Module.test_env_popup).is_displayed():
                self.driver.find_element(*Search_Module.test_env_continue_btn).click()
                self.driver.find_element(*Search_Module.test_instru_next_btn).click()
                try:
                    self.driver.find_element(*Search_Module.test_instru_checkbox_btn).click()
                    self.driver.find_element(*Search_Module.test_i_am_ready_to_begin_btn).click()
                    time.sleep(10)
                    self.take_test()
                except:
                    print("The Test got Expired")


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


