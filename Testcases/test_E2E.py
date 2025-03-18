import time
import pytest

from Pages.achievehome import achieve_home
from Pages.landingPages import landingpages
from Pages.practicehome import PracticeHome
from Pages.profile_menu import Profile_Menu
from Pages.searchpage import Search_Module
from Pages.learnhome import LearnHome
from Pages.testhome import TestHome
from Pages.userhome import UserHome
from Testcases.Baseclass import BaseClass


class TestEmbibeApp(BaseClass):

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def _login_with_password(self):
        lp = landingpages(self.driver)
        lp.signinusingpassword()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_login_with_password(self):
        self._login_with_password()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_login_with_OTP(self):
        lp = landingpages(self.driver)
        lp.signinusingOTP()
        # log = self.getLogger()
        # log.info("Testcase 2 : User Logs in via OTP")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_forgot_password(self):
        lp = landingpages(self.driver)
        lp.clickforgotpassword()
        # log = self.getLogger()
        # log.info("Testcase 3 : User clicks Forgot Password")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_click_tos(self):
        lp = landingpages(self.driver)
        lp.clickTOS()
        # log = self.getLogger()
        # log.info("Testcase 4: User clicks on Terms and Conditions link")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_click_PP(self):
        lp = landingpages(self.driver)
        lp.clickPrivacyPolicy()
        # log = self.getLogger()
        # log.info("Testcase 5: User clicks on Privacy Policy link")

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_tos_in_signinpage(self):
        lp = landingpages(self.driver)
        lp.tosinsigninpage()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_privacy_policy_in_signinpage(self):
        lp = landingpages(self.driver)
        lp.privacypolicyinsigninpage()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_edit_goal_exam(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_edit_goal()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_guided_tour(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.guided_tour()
        time.sleep(2)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_module_click(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.module_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_trending_video_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.trending_videos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def trending_videos_more_topic_videos_click(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.trending_videos_more_topic_videos_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_trending_videos_related_video_click(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.trending_videos_related_video_click()
    #
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_embibe_explainer_video_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.embibe_explainer_videos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_embibe_explainer_more_topic_videos_click(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.embibe_explainers_more_topic_videos_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_embibe_explainer_related_video_click(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.embibe_explainers_related_video_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_books_with_videos_solutions_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.books_with_videos_solutions()


    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_chapter_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_chapters()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_PTR_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_ptr()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_sincerity_score_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_sincerity_score()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_embibe_explainers_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_embibe_explainers()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_topics_in_this_chapter_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_topics_in_this_chapter()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_learn_prerequisite_topics_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.learn_prerequisite_topics()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_taking_in_chapter_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.test_taking_in_learn_chapter()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_practice_taking_in_chapter_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.practice_taking_in_chapter()
        time.sleep(3)

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_continue_learning_tile(self):
        self._login_with_password()
        LH = LearnHome(self.driver)
        LH.continue_learning()
        time.sleep(3)
    #
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_five_mins_custom_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.five_mins_custom_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_custom_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.custom_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.cyot
    def test_trending_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.trending_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_recommended_learning_to_ace_this_trending_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.recommended_learning_to_ace_in_trending_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_recommended_practice_to_ace_in_trending_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.recommended_practice_to_ace_in_trending_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_more_test_taking_in_trending_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.more_test_taking_in_trending_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_full_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.full_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_recommended_learning_to_ace_this_full_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.recommended_learning_to_ace_this_full_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_recommended_practice_to_ace_this_full_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.recommended_practice_to_ace_this_full_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_more_test_taking_in_full_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.more_test_taking_in_full_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_chapter_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.chapter_test()

    def test_recommended_learning_to_ace_this_chapter_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.recommended_learning_to_ace_this_chapter_test()

    def test_recommended_practice_to_ace_this_chapter_test_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.recommended_practice_to_ace_this_chapter_test()

    def test_more_test_taking_in_chapter_tile(self):
        self._login_with_password()
        TH = TestHome(self.driver)
        TH.more_test_taking_in_chapter_test()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_module(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_module_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_video(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_learn_video_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.searchh
    def test_search_practice(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_practice_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_questions(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_question_click()
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_books(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_book_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_ptr(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_PTR_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_search_test(self):
        self._login_with_password()
        SM = Search_Module(self.driver)
        SM.search_test_and_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_profile_menu(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_manage_profile()


    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_edit_profile(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_edit_profile_name()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_profile_menu_settings(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_settings()
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_tos(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_tos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_privacy_policy(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_privacy_policy()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_help_center(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_help_center()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_menu_feedback(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_help_center()

    # @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    # def test_UH_module_click(self):
    #     self._login_with_password()
    #     UH = UserHome(self.driver)
    #     UH.UH_module_click()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_add_fav_book_click(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_add_fav_books()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_test_i_have_taken(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_Test_i_have_taken()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_bookmark_videos(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_bookmark_videos()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_bookmark_questions(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_bookmark_questions()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.test
    def test_menu_signout(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_sign_out()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_UH_embibe_big_books(self):
        self._login_with_password()
        UH = UserHome(self.driver)
        UH.UH_embibe_big_books()


    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practicee
    def test_practice_chapter(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.practice_chapter_tile()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_practice_sincerity_score(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.sincerity_score_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_practice_attempt_quality_jar(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.attempt_quality_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_practice_chapter_PTR(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.PTR_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_topic_practice_chapter(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.topic_practice_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_practice_chapter_more_test(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.more_test_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_recommended_learning_chapter(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.recommended_learning_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_recommended_learning_chapter(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.more_test_in_practice_chapter()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_embibe_author_books(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.embibe_author_book()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.practice
    def test_embibe_big_books(self):
        self._login_with_password()
        PH = PracticeHome(self.driver)
        PH.embibe_big_book()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_profile_menu_change_language(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.menu_change_lang()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    def test_hero_banner_change_goal_exam(self):
        self._login_with_password()
        PM = Profile_Menu(self.driver)
        PM.hero_banner_change_goal_exam()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_achieve_create_DT1(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.create_diagnostic_test()
    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achievee
    def test_achieve_start_DT1(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.start_diagnostic_test1()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_achieve_start_DT2(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.start_diagnostic_test2()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_achieve_explore_mastery(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.explore_mastery_tile()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_generate_PAJ(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.create_PAJ_journey()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_achieve_I_will_take_test_later(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.i_will_start_test_later()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_start_PAJ_journey(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.start_PAJ()

    @pytest.mark.usefixtures("appiumdriver", "log_on_failure")
    @pytest.mark.achieve
    def test_achieve_full_journey(self):
        self._login_with_password()
        AH = achieve_home(self.driver)
        AH.achieve_full_journey()











