import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(__file__)

HAS_SAML2 = False # supports the SSO interface provided by the Up2U project (www.up2uiversity.eu) ?
HAS_LRS = False # supports xAPI?
HAS_EARMASTER = False # supports import and processing of the data exported from the EarMaster application ?

from commons.settings import *

PRIMARY_DOMAIN = 'health.commonspaces.eu'
SECONDARY_DOMAIN = None
TEST_DOMAIN = None

SITE_ID = 3
SITE_NAME = 'HEALTH'
SITE_ROOT = 'health'
ALLOW_REDUCED_PROFILE = True

WSGI_APPLICATION = 'health.wsgi.application'
ROOT_URLCONF = 'health.urls'

PROJECT_TITLE = 'HEALTH - Health Emergency in Asia and Africa'
PROJECT_NAME = 'health'
LOGIN_REDIRECT_URL = 'health.home'
