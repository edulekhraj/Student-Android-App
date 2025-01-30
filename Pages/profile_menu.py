import time
from appium.webdriver.common.appiumby import AppiumBy
from Utilities import configReader


class Profile_Menu:


    def __init__(self, driver):
        self.driver = driver

    profile_icon = AppiumBy.ID, 'com.embibe.student:id/img_HeroBannerAvatar'
    manage_profile = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Manage Profiles"]'
    edit_profile = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/ivEdit"])[1]'
    edit_goal = AppiumBy.ID, 'com.embibe.student:id/editGoalsBtn'
    exam_search_field = AppiumBy.ID, 'com.embibe.student:id/autoTvSearchExam'
    exam_selection = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_layput_parent"])[1]'
    lang_done_btn = AppiumBy.ID, 'com.embibe.student:id/tv_done'
    settings = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Settings"]'
    change_lang = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_more_option"])[5]'
    tos = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Terms & Conditions"]'
    privacy_policy = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Privacy Policy"]'
    help_center = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Help Center"]'
    feed_back = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Feedback"]'
    feed_back_text = AppiumBy.ID, 'com.embibe.student:id/et_comment_box'
    feed_back_submit_btn = AppiumBy.ID, 'com.embibe.student:id/btn_submit_feedback'
    sign_out = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_more" and @text="Sign Out"]'
    sign_out_no = AppiumBy.ID, 'com.embibe.student:id/btn_quit'
    sign_out_yes = AppiumBy.ID, 'com.embibe.student:id/btn_sign_out'
    guided_tour_cancel_btn = AppiumBy.ID, 'com.embibe.student:id/ivClose'
    menu_back_btn = AppiumBy.ID, 'com.embibe.student:id/ivBack'
    profile_name_field = AppiumBy.ID, 'com.embibe.student:id/username'
    avatar_edit_btn = AppiumBy.ID, 'com.embibe.student:id/edit'
    avatar_1 = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.embibe.student:id/iv_avatar"])[1]'
    profile_save_btn = AppiumBy.ID, 'com.embibe.student:id/btn_save'
    exam_button = AppiumBy.ID, 'com.embibe.student:id/txt_heroBanner_action_goal_switch'
    exam_search_btn = AppiumBy.ID, 'com.embibe.student:id/autoTvSearchExam'
    goal_selection = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_layput_parent"])[1]'
    goal_lang_done_btn = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.student:id/tv_done"]'
    lang_two_btn = AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.embibe.student:id/cl_language"])[3]'
    lang_one_btn = AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.embibe.student:id/cl_language'])[2]"
    cancel_btn = AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.embibe.student:id/btn_cancel"]'

    def hero_banner_change_goal_exam(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.exam_button).click()
        self.driver.find_element(*Profile_Menu.exam_search_btn).click()
        self.driver.find_element(*Profile_Menu.exam_search_btn).send_keys(configReader.readConfig('prod', 'exam'))
        self.driver.find_element(*Profile_Menu.goal_selection).click()
        self.driver.find_element(*Profile_Menu.lang_two_btn).click()
        self.driver.find_element(*Profile_Menu.cancel_btn).click()
        self.driver.find_element(*Profile_Menu.goal_lang_done_btn).click()
        time.sleep(10)

    def menu_manage_profile(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.manage_profile).click()
        time.sleep(2)

    def menu_edit_goal(self):
        self.menu_manage_profile()
        self.driver.find_element(*Profile_Menu.edit_profile).click()
        self.driver.find_element(*Profile_Menu.edit_goal).click()
        self.driver.find_element(*Profile_Menu.exam_search_field).click()
        self.driver.find_element(*Profile_Menu.exam_search_field).send_keys(configReader.readConfig('prod', 'exam'))
        time.sleep(3)
        self.driver.find_element(*Profile_Menu.exam_selection).click()
        self.driver.find_element(*Profile_Menu.lang_done_btn).click()
        time.sleep(5)
        self.driver.find_element(*Profile_Menu.menu_back_btn).click()

    def menu_edit_profile_name(self):
        self.menu_manage_profile()
        self.driver.find_element(*Profile_Menu.edit_profile).click()
        self.driver.find_element(*Profile_Menu.profile_name_field).click()
        self.driver.find_element(*Profile_Menu.profile_name_field).clear()
        time.sleep(2)
        self.driver.find_element(*Profile_Menu.profile_name_field).click()
        self.driver.find_element(*Profile_Menu.profile_name_field).send_keys(configReader.readConfig('prod', 'student_name'))
        self.driver.find_element(*Profile_Menu.avatar_edit_btn).click()
        self.driver.find_element(*Profile_Menu.avatar_1).click()
        self.driver.find_element(*Profile_Menu.profile_save_btn).click()

    def menu_settings(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.settings).click()
        time.sleep(2)

    def menu_change_lang(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.change_lang).click()
        time.sleep(3)
        self.driver.find_element(*Profile_Menu.lang_one_btn).click()
        # self.driver.find_element(*Profile_Menu.cancel_btn).click()
        self.driver.find_element(*Profile_Menu.goal_lang_done_btn).click()
        time.sleep(5)

    def menu_tos(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.tos).click()
        time.sleep(2)

    def menu_privacy_policy(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.privacy_policy).click()
        time.sleep(2)

    def menu_help_center(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.help_center).click()
        time.sleep(2)

    def menu_feedback(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        time.sleep(2)
        self.driver.find_element(*Profile_Menu.feed_back).click()
        time.sleep(2)
        self.driver.find_element(*Profile_Menu.feed_back_text).send_keys("QA Test")
        self.driver.find_element(*Profile_Menu.feed_back_submit_btn).click()

    def menu_sign_out(self):
        self.driver.find_element(*Profile_Menu.guided_tour_cancel_btn).click()
        self.driver.find_element(*Profile_Menu.profile_icon).click()
        self.driver.find_element(*Profile_Menu.sign_out).click()
        self.driver.find_element(*Profile_Menu.sign_out_no).click()
        self.driver.find_element(*Profile_Menu.sign_out).click()
        self.driver.find_element(*Profile_Menu.sign_out_yes).click()
        time.sleep(5)
