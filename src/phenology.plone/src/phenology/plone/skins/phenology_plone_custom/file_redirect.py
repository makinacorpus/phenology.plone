## Script (Python) "file_redirect"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
from Products.CMFCore.utils import getToolByName

mtool = getToolByName(context, 'portal_membership')
can_edit = mtool.checkPermission('Modify portal content', context)

if not can_edit:
    url = context.absolute_url()
    return context.REQUEST.RESPONSE.redirect(url)
else:
    return context.file_view()
