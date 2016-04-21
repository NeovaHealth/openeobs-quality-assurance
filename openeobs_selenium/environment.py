"""Configuration file for the database"""

# odoo credential
USERNAME = 'admin'
PASSWORD = 'admin'
# DB names
TEST_DB_NAME = 'openeobs_quality_assurance_db'
DATABASE = 'slam'
# Url Info
ODOO_CLIENT_URL = 'http://localhost:8069'
# DESKTOP_URL = 'http://localhost:8069/web?db={database}'.format(
#     database=DATABASE)
DESKTOP_URL = ODOO_CLIENT_URL+'/web?db={database}'.format(database=DATABASE)

def get_desktop_url():
    return ODOO_CLIENT_URL+'/web?db={database}'.format(database=DATABASE)
# MOB_LOGIN = 'http://localhost:8069/mobile/login'
MOB_LOGIN = ODOO_CLIENT_URL + '/mobile/login'
PATIENT_PAGE = ODOO_CLIENT_URL + '/mobile/patient/'
TASK_PAGE = ODOO_CLIENT_URL + '/mobile/task/'

# Nurse Login detail
NURSE_USERNM1 = 'nasir'
NURSE_PWD1 = 'nasir'

# Senior Manager login credential
SM_USERNM1 = 'saint'
SM_PWD = 'saint'

#HCA login credential
HCA_USERNM1 = 'hal'
HCA_PWD1 = 'hal'

#Doctor login credential
DOCTOR_USERNM1 = 'david'
DOCTOR_PWD1 = 'david'
