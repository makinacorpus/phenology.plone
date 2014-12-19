#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plone import api
from plone.app.multilingual.browser.setup import SetupMultilingualSite
from plone.app.textfield.value import RichTextValue
from plone.tiles.interfaces import ITileDataManager

COVER_ID = "homepage"
COVER_TITLE = "Phenoclim"
COVER_LAYOUT = """[{"type": "row", "children": [{"data": {"layout-type": "column", "column-size": 12}, "type": "group", "children": [{"tile-type": "collective.cover.richtext", "type": "tile", "id": "top-banner"}], "roles": ["Manager"], "id": "group1"}]}, {"type": "row", "children": [{"data": {"layout-type": "column", "column-size": 12}, "type": "group", "children": [{"tile-type": "collective.cover.collection", "type": "tile", "id": "slideshow"}], "roles": ["Manager"]}]}, {"type": "row", "children": [{"data": {"layout-type": "column", "column-size": 8}, "type": "group", "children": [{"tile-type": "collective.cover.richtext", "type": "tile", "id": "middle-banner"}], "roles": ["Manager"]}, {"data": {"layout-type": "column", "column-size": 4}, "type": "group", "children": [{"tile-type": "collective.cover.embed", "type": "tile", "id": "twitter-tile"}], "roles": ["Manager"]}]}]"""
RICHTEXT_TILES = [
    {
        'id': 'top-banner',
        'content': """<table class="invisible">
<tbody>
<tr><th>
<p>Phénoclim est un programme scientifique et pédagogique<br />qui invite le public à mesure l'impact du changement climatique<br />sur la végétation en montage. </p>
<div></div>
</th><th><a href="#">Inscrivez-vous !</a></th></tr>
</tbody>
</table>""",
    },
    {
        'id': 'middle-banner',
        'content': """<table>
<tbody>
<tr>
<td>
<h2>Carte des observateurs</h2>
<p>Lorem</p>
</td>
<td><img class="image-inline" src="resolveuid/1123a278e32f4d71a12423220b78db9a" /></td>
</tr>
</tbody>
</table>""",
    },
]
EMBED_TILES = [
    {
        'id': 'twitter-tile',
        'content': """<a class="twitter-timeline"  href="https://twitter.com/creamontblanc" data-widget-id="545531077637701634">Tweets de @creamontblanc</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>""",
    }
]
COLLECTION_TILES = [
    {
        'id': 'slideshow',
        'collection': 'news',
        'slidemode': True,
        'config': {'description': {'order': u'4', 'visibility': u'on'}, 'title': {'htmltag': u'h2', 'order': u'2', 'visibility': u'on'}, 'css_class': u'tile-default', 'image': {'position': u'right', 'imgsize': u'large 768:768', 'visibility': u'on', 'order': u'0'}, 'footer': {'visibility': u'off', 'order': u'7', 'htmltag': u'h2'}, 'slidemode': {'order': u'9', 'visibility': u'on'}, 'header': {'htmltag': u'h2', 'order': u'1', 'visibility': u'on'}, 'offset': {'order': u'6', 'visibility': u'on', 'offset': u'0'}, 'date': {'order': u'3', 'visibility': u'on'}, 'number_to_show': {'order': u'5', 'visibility': u'on', 'size': u'5'}},
    }
]

def create_cover(folder, purge=False):
    portal = api.portal.get()
    if purge and COVER_ID in folder.objectIds():
        folder.manage_delObjects([COVER_ID])

    if COVER_ID not in folder:
        folder.invokeFactory(
            'collective.cover.content',
            COVER_ID,
            title=COVER_TITLE
        )
        wtool = folder.portal_workflow
        wtool.doActionFor(folder[COVER_ID], 'publish')

    cover = folder[COVER_ID]
    cover.cover_layout = COVER_LAYOUT

    # richtext
    for data in RICHTEXT_TILES:
        tile = cover.restrictedTraverse(
            '@@{0}/{1}'.format('collective.cover.richtext', data["id"])
        )
        value = RichTextValue(raw=data["content"],
            mimeType='text/x-html-safe',
            outputMimeType='text/x-html-safe')
        data_mgr = ITileDataManager(tile)
        data_mgr.set({'text': value})

    # embed tiles blocks
    for data in EMBED_TILES:
        tile = cover.restrictedTraverse(
            '@@{0}/{1}'.format('collective.cover.embed', data["id"])
        )
        data_mgr = ITileDataManager(tile)
        data_mgr.set({'embed': data["content"]})

    # embed tiles blocks
    for data in COLLECTION_TILES:
        tile = cover.restrictedTraverse(
            '@@{0}/{1}'.format('collective.cover.collection', data["id"])
        )
        if not data['collection'] in folder:
            news_fr = portal['fr'][data['collection']]
            api.content.copy(source=news_fr, target=folder)
        obj = folder[data['collection']].aggregator
        tile.populate_with_object(obj)
        tile.set_tile_configuration(data['config'])

    folder.setDefaultPage(COVER_ID)

def init_content(context):
    portal = api.portal.get()
    setupTool = SetupMultilingualSite()
    setupTool.setupSite(portal)
    setupTool.move_default_language_content()
    for lang in ['fr', 'en', 'it']:
        create_cover(portal[lang])