import logging
from zope.i18nmessageid import MessageFactory

MessageFactory = phenologyploneMessageFactory = MessageFactory('phenology.plone')
logger = logging.getLogger('phenology.plone')
EXTENSION_PROFILES = ('phenology.plone:default',)
SKIN = 'phenology.skin'
PRODUCT_DEPENDENCIES = (
)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


GLOBALS = globals()
