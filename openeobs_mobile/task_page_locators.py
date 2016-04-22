"""Helpers for the task page"""
from selenium.webdriver.common.by import By


PATIENT_NAME_CONTAINER = (By.ID, 'patientName')
PATIENT_NAME_LINK = (By.CSS_SELECTOR, '#patientName > a')
PATIENT_NAME_INFO = (By.CSS_SELECTOR, '#patientName .icon-info')
PATIENT_INFO_POPUP = (By.ID, 'patient_info')
PATIENT_INFO_POPUP_TITLE = (By.TAG_NAME, 'h2')
PATIENT_INFO_POPUP_FSCREEN_BTN = (By.ID, 'patient_obs_fullscreen')
PATIENT_INFO_FULLSCREEN = (By.CSS_SELECTOR, '.no-scroll > .full-modal')
PATIENT_INFO_FULLSCREEN_IFRAME = (By.TAG_NAME, 'iframe')
PATIENT_INFO_FULLSCREEN_CLOSE = (By.ID, 'closeFullModal')
TASK_FORM = (By.ID, 'obsForm')
TASK_FORM_TASK_ID = (By.NAME, 'taskId')
TASK_FORM_START_TIME = (By.ID, 'startTimestamp')
TASK_FORM_SUBMIT = (By.ID, 'submitButton')
TASK_FORM_INPUT_FIELD = (By.CLASS_NAME, 'obsField')
TASK_FORM_FIELD_LABEL = (By.CSS_SELECTOR, '.input-header > label')
TASK_FORM_FIELD_INPUT = (By.CSS_SELECTOR, '.input-header > input')
TASK_FORM_FIELD_SELECT = (By.CSS_SELECTOR, '.input-body > select')
TASK_FORM_FIELD_ERRORS = (By.CSS_SELECTOR, '.input-body > .errors')
TASK_FORM_FIELD_HELP = (By.CSS_SELECTOR, '.input-body > .help')
TASK_FORM_INVALID_SUBMIT = (By.ID, 'invalid_form')
CONFIRM_ACTION = (By.CSS_SELECTOR, '#submitButton')
CONFIRM_SUBMIT = (
    By.CSS_SELECTOR, '#submit_observation > ul > li:nth-child(2) > a')
SUCCESSFUL_SUBMIT = (By.CSS_SELECTOR, '#submit_success > h2')
CONFIRM_TASK = (By.CSS_SELECTOR, '#submit_success > ul > li:nth-child(2) > a')
CANCEL_SUBMIT = (By.ID, 'cancelSubmit')
CONFIRM_CANCEL = (By.CSS_SELECTOR,
                  '.options > li:nth-child(2) > a:nth-child(1)')
SUCCESSFUL_CANCEL = (By.CSS_SELECTOR, '#cancel_success > h2:nth-child(1)')
RELATED_TASK = (By.CSS_SELECTOR, '#submit_success > .dialogContent')
TASK = (By.CLASS_NAME, 'taskInfo')
GO_TO_MY_TASK = (By.XPATH, '//a[contains(.,"Go to My Tasks")]')
MEDIUM_SLAM_TASKS = (By.XPATH, "//*]contains(text(), 'Urgently inform medical team')]")
CLINICAL_RISK = (By.CSS_SELECTOR,'#submit_observation > div > p:nth-child(1) > strong')
CONFIRM_ACTION_TAKEN = (By.CSS_SELECTOR, '#obsForm > p')
RELATED_TASK_LIST = (By.CSS_SELECTOR, '#submit_success > div > ul > li > a')
CONFIRM_AMBULANCE = (By.CSS_SELECTOR, '#obsForm > p:nth-child(2)')
