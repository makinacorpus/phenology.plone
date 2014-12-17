from plone import api
from plone.app.multilingual.browser.setup import SetupMultilingualSite

def upgrade_1001(context):
    portal = api.portal.get()
    setupTool = SetupMultilingualSite()
    setupTool.setupSite(portal)