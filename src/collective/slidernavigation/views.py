from zope.site.hooks import getSite
from zope.publisher.browser import BrowserView

import logging

log = logging.getLogger("collective.slidernavigation.views:")


class PaneContentView(BrowserView):
    """ Return pane content as HTML and will be called by AJAX request.
    """

    def __call__(self, uid=None):
        """
        """
        self.pane_content = {}
        self.pane_content = self.get_pane_content(uid)
        return self.index()


    def get_pane_content(self, uid=None):
        """ Return pane content as dict.
        """
        portal = getSite()
        portal_catalog = portal.portal_catalog
        query = {}
        if not uid:
            uid = self.request.get("pane_content_uid")
        print uid
        if not uid:
            log.debug("no uid given!")
            return

        query["UID"] = uid
        results = portal_catalog(query)
        if not results:
            log.debug("no results for given uid '%s' !" % uid)
            return

        brain = results[0]
        pane_content = {}
        pane_content["id"] = brain.id
        pane_content["title"] = brain.Title
        pane_content["description"] = brain.Description
        pane_content["url"] = brain.getURL()
        if brain.hasContentLeadImage:
            pane_content["img_base_url"] = pane_content["url"]
        else:
            pane_content["img_base_url"] = ''
        link_query = {}
        link_query["portal_type"] = 'Link'
        link_query["path"] = {'query': brain.getPath(), 'depth':1}
        link_query["sort_on"] = 'getObjPositionInParent'
        link_results = portal_catalog(link_query)
        pane_content["links"] = [{'title': link.Title, 'url': link.getRemoteUrl}\
                for link in link_results]
        log.debug("pane content: %s" % pane_content)
        return pane_content



