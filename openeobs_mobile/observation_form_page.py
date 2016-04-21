from openeobs_mobile.page_helpers import BasePage
from openeobs_mobile.task_page_locators import TASK_FORM_SUBMIT
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class ObservationFormPage(BasePage):
    def enter_obs_data(self, data):
        """
        Enter data into an observation form
        :param data: The data to be entered
        """
        if 'oxygen_administration_flag' in data:
            oxy = self.driver.find_element_by_name(
                'oxygen_administration_flag')
            oxy_select = Select(oxy)
            oxy_select.select_by_visible_text(
                data['oxygen_administration_flag'])

            if 'device_id' in data:
                device = self.driver.find_element_by_name('device_id')
                device_select = Select(device)
                device_select.select_by_visible_text(data['device_id'])

        for field, value in data.iteritems():
            input_field = self.driver.find_element_by_name(field)
            input_field.send_keys(value)
            input_field.send_keys(Keys.TAB)

        self.driver.find_element(*TASK_FORM_SUBMIT).click()