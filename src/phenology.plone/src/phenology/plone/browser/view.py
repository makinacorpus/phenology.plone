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
    def hasSubSections(self, folder_id):
        if len(self.getSubSections(folder_id)) > 0 :
            return True
        return False

    @memoize
    def getSubSections(self, folder_id):
        root = api.portal.get_navigation_root(self.context)
        catalog = api.portal.get_tool(name='portal_catalog')
        navtree_properties = root.portal_properties.navtree_properties
        blacklist = navtree_properties.getProperty('metaTypesNotToList', ())
        all_types = catalog.uniqueValuesFor('portal_type')

        subsections = catalog(
            path={
                'query' : '/'.join(root.getPhysicalPath() + (folder_id,)),
                'depth': 1,
            },
            exclude_from_nav=False,
            portal_type=[t for t in all_types if t not in blacklist],
            sort_on='getObjPositionInParent', sort_order='ascending'
        )
        return [sub.getObject() for sub in subsections]

    @memoize
    def getDescription(self):
        root = api.portal.get_navigation_root(self.context)
        description = root.Description()
        return description
