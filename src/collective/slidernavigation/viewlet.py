from zope.site.hooks import getSite
from plone.app.layout.viewlets.common import ViewletBase


class SliderNavigation(ViewletBase):
    """ SliderNavigation viewlet
    """

    def update(self):
        """
        """
        self.portal = getSite()
        self.current_url = self.portal.portal_url
        self.children = self.get_children()

    def get_children(self):
        """ return filtered navigation children of the curent folder
        """
        portal_catalog = self.portal.portal_catalog
        path = '/'.join(self.context.getPhysicalPath())
        query={
            'path': {'query': path},
            'portal_type': 'Folder',
            'sort_on': 'getObjPositionInParent'
        }
        results = portal_catalog(query)
        children = [child for child in results
                if not child.exclude_from_nav and not child.id == self.context.id]
        return children

