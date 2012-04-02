from zope.site.hooks import getSite
from zope.publisher.browser import BrowserView

import logging

log = logging.getLogger("collective.slidernavigation.views:")


class PaneContentView(BrowserView):
    """ Return pane content as HTML and will be called by AJAX request.
    """

    def __call__(self):
        """
        """
        self.pane_content = {}
        self.pane_content = self.get_pane_content()
        return self.index()


    def get_pane_content(self):
        """ Return pane content as dict.
        """
        portal = getSite()
        portal_catalog = portal.portal_catalog
        query = {}
        uid = self.request.get("pane_content_uid")
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
        log.debug("pane content: %s" % pane_content)
        return pane_content



