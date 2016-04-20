"""Tests to ensure that the patient info displays correctly"""
from openeobs_mobile.list_page import ListPage
from openeobs_mobile.login_page import LoginPage
from openeobs_mobile.page_confirm import PageConfirm
from openeobs_mobile.task_page import TaskPage
from openeobs_mobile.task_page_locators import PATIENT_NAME_LINK, \
    PATIENT_NAME_INFO, PATIENT_INFO_POPUP_TITLE, \
    PATIENT_INFO_FULLSCREEN_IFRAME, PATIENT_INFO_FULLSCREEN_CLOSE
from openeobs_selenium.environment import MOB_LOGIN, NURSE_PWD1, NURSE_USERNM1, \
    TASK_PAGE, PATIENT_PAGE
from tests.test_common import TestCommon


class TestTaskPagePatientInfo(TestCommon):
    """
    Setup a session and test that the patient info is correct
    """
    def setUp(self):
        self.driver.get(MOB_LOGIN)
        self.login_page = LoginPage(self.driver)
        self.list_page = ListPage(self.driver)
        self.task_page = TaskPage(self.driver)
        self.login_page.login(NURSE_USERNM1, NURSE_PWD1)
        self.list_page.go_to_task_list()
        tasks = self.list_page.get_list_items()
        task_to_test = tasks[0]
        self.task_url = task_to_test.get_attribute('href')
        self.driver.get(self.task_url)

    def test_can_logout(self):
        """
        Test that the title of the login page is Open-eObs
        """
        self.task_page.logout()
        self.assertTrue(PageConfirm(self.driver).is_login_page(),
                        'Did not get to the logout page correctly')

    def test_can_go_to_task_list_page(self):
        """
        Test that can go to task list page
        """
        self.task_page.go_to_task_list()
        self.assertTrue(PageConfirm(self.driver).is_task_list_page(),
                        'Did not get to the task list page correctly')

    def test_go_to_patient_list_page(self):
        """
        Test that can go to the patient list page
        """
        self.task_page.go_to_patient_list()
        self.assertTrue(PageConfirm(self.driver).is_patient_list_page(),
                        'Did not get to patient list page correctly')

    def test_can_go_to_stand_in_page(self):
        """
        Test that can navigate to the stand in page
        """
        self.task_page.go_to_standin()
        self.assertTrue(PageConfirm(self.driver).is_stand_in_page(),
                        'Did not get to stand in page correctly')

    def test_can_carry_out_barcode_scan(self):
        """
        Test that can do a barcode scan
        """
        task_id = self.task_url.replace(
            TASK_PAGE, ''
        )
        id_to_use = self.task_page.task_scan_helper(int(task_id))
        self.task_page.do_barcode_scan(id_to_use['other_identifier'])

    def test_patient_info_name(self):
        """
        Test that can get the patient info popup on pressing patient name
        """
        patient_name_button = self.driver.find_element(
            *PATIENT_NAME_LINK
        )
        patient_id = patient_name_button.get_attribute('patient-id')

        popup = self.task_page.open_patient_info()
        popup_header = popup.find_element(
            *PATIENT_INFO_POPUP_TITLE
        )
        patient_data = self.task_page.patient_helper(int(patient_id))[0]
        popup_title = '{0} {1}'.format(patient_data['full_name'],
                                       patient_data['gender'])

        self.assertEqual(popup_title, popup_header.text.replace('\n', ' '),
                         'Incorrect popup name')

    def test_patient_info_button(self):
        """
        Test that can get the patient info popup on pressing patient name
        """
        patient_name_button = self.driver.find_element(
            *PATIENT_NAME_INFO
        )
        patient_id = patient_name_button.get_attribute('patient-id')

        popup = self.task_page.open_patient_info()
        popup_header = popup.find_element(
            *PATIENT_INFO_POPUP_TITLE
        )
        patient_data = self.task_page.patient_helper(int(patient_id))[0]
        popup_title = '{0} {1}'.format(patient_data['full_name'],
                                       patient_data['gender'])
        self.assertEqual(popup_title, popup_header.text.replace('\n', ' '),
                         'Incorrect popup name')

    def test_press_obs_data_button(self):
        """
        Test that pressing the 'View Patient Observation Data' shows the
        patient page in a fullscreen modal
        """
        patient_name_button = self.driver.find_element(
            *PATIENT_NAME_INFO
        )
        patient_id = patient_name_button.get_attribute('patient-id')
        fullscreen = self.task_page.open_full_patient_obs_data()
        iframe = fullscreen.find_element(
            *PATIENT_INFO_FULLSCREEN_IFRAME
        )
        iframe_url = iframe.get_attribute('src')
        patient_url = PATIENT_PAGE+'{0}'.format(
            patient_id
        )
        self.assertEqual(iframe_url, patient_url, 'Incorrect iframe src url')

    def test_close_full_obs_modal(self):
        """
        Test that can close the fullscreen modal
        """
        fullscreen = self.task_page.open_full_patient_obs_data()
        close_button = fullscreen.find_element(
            *PATIENT_INFO_FULLSCREEN_CLOSE
        )
        close_button.click()
        self.assertTrue(self.task_page.fullscreen_not_open(),
                        'Fullscreen did not close')
