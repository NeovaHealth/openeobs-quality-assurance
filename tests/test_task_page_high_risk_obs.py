"""Test to ensure that a high risk NEWS ob works correctly"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.data import HIGH_RISK_SCORE_9_EWS_DATA, HIGH_SCORE_RESPONSE
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.patient_page import PatientPage
from openeobs_mobile.patient_page_locators import OPEN_OBS_MENU_NEWS_ITEM
from openeobs_mobile.task_page_locators import CONFIRM_SUBMIT, RELATED_TASK
from openeobs_selenium.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1
from tests.test_common import TestCommon


class TestHighRiskPage(TestCommon):
    """
    Setup a session and test that a high risk NEWS observation
    can be submitted, and that the correct action triggers
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_patient_list()

    def test_high_risk_obs(self):
        """
        Test that an 'immediately inform medical team' task is triggered
        after a high NEWS score
        """
        high_score = HIGH_RISK_SCORE_9_EWS_DATA

        patients = self.patient_list_page.get_list_items()

        PatientPage(self.driver).select_patient(patients)
        PatientPage(self.driver).open_form(OPEN_OBS_MENU_NEWS_ITEM)
        PatientPage(self.driver).enter_obs_data(high_score)

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(CONFIRM_SUBMIT)
        )

        self.driver.find_element(*CONFIRM_SUBMIT).click()

        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(RELATED_TASK)
        )
        response = self.driver.find_element(*RELATED_TASK)

        self.assertEqual(HIGH_SCORE_RESPONSE, response.text,
                         'Incorrect triggered action for high risk ob')
