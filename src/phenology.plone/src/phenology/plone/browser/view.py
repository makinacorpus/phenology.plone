# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

from plone import api
from plone.memoize.view import memoize
from Products.Five import BrowserView
from zope import interface


class IPhenologyView(interface.Interface):
    """Marker interface"""


class PhenologyView(BrowserView):
    """
    """
    interface.implements(IPhenologyView)

    @memoize
    def getSubSections(self, folder_id):
        root = api.portal.get_navigation_root(self.context)
        catalog = api.portal.get_tool(name='portal_catalog')
        subsections = catalog(
            path={
                'query' : '/'.join(root.getPhysicalPath() + (folder_id,)),
                'depth': 1,
            },
            exclude_from_nav=False,
        )
        return subsections