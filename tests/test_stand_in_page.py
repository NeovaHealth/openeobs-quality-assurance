"""Tests to ensure that the stand in page works correctly"""
import selenium.webdriver.support.expected_conditions as ec
import selenium.webdriver.support.ui as ui
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.stand_in_page import StandInPage
from openeobs_mobile.stand_in_page_locators import STAND_IN_ACCEPT_BUTTON, \
    STAND_IN_CONFIRM, STAND_IN_ERROR
from openeobs_selenium.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1
from tests.test_common import TestCommon


class TestStandInPage(TestCommon):
    """
    Setup a session and test the stand in page
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.patient_list_page = ListPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.patient_list_page.go_to_standin()

    def test_stand_in(self):
        """
        Test that the stand-in function works
        """
        nurse_name = StandInPage(self.driver).submit_stand_in()
        nurse = nurse_name.split(' ', 1)[0].lower()

        response = StandInPage(self.driver).confirm_stand_in(
            nurse, self.patient_list_page).text

        self.patient_list_page.go_to_standin()

        success = 'Successfully accepted stand-in invite'
        self.assertEqual(success, response,
                         'Stand in was unsuccessful')

    def test_stand_in_reject(self):
        """
        Test that a stand-in can be rejected
        """
        nurse_name = StandInPage(self.driver).submit_stand_in()
        nurse = nurse_name.split(' ', 1)[0].lower()
        response = StandInPage(self.driver).reject_stand_in(
            nurse, self.patient_list_page)

        success = 'Successfully rejected stand-in invite'
        self.assertEqual(success, response.text, 'Reject was unsuccessful')

    def test_claim_stand_in(self):
        """
        Test that a stand-in can be claimed back
        """
        nurse_name = StandInPage(self.driver).submit_stand_in()
        nurse = nurse_name.split(' ', 1)[0].lower()
        StandInPage(self.driver).confirm_stand_in(
            nurse, self.patient_list_page)

        self.setUp()

        response = StandInPage(self.driver).claim_stand_in()

        success = 'Patients claimed'
        self.assertEqual(success, response.text, 'Reject was unsuccessful')

    def test_erppeek_stand_in(self):
        """
        Test that accepting a stand-in through the GUI, after doing so through
        erppeek will cause a server error
        """
        task_id = StandInPage.add_stand_in()
        StandInPage(self.driver).go_to_patient_list()
        StandInPage.complete_stand_in(task_id)

        self.driver.find_element(*STAND_IN_ACCEPT_BUTTON).click()
        ui.WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(STAND_IN_CONFIRM))
        self.driver.find_element(*STAND_IN_CONFIRM).click()
        response = self.driver.find_element(*STAND_IN_ERROR).text

        success = 'Error accepting patients'
        self.assertEqual(success, response, 'Stand in should not be accepted')
