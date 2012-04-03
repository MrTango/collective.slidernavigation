from Acquisition import aq_inner, aq_parent
from zope.component import getMultiAdapter
from zope.site.hooks import getSite
from plone.app.layout.viewlets.common import ViewletBase


class SliderNavigation(ViewletBase):
    """ SliderNavigation viewlet
    """

    def update(self):
        """
        """
        self.portal = getSite()
        self.base_url = self.portal.portal_url
        self.cpath = '/'.join(self.context.getPhysicalPath())
        self.children = self.get_children()

    def get_children(self):
        """ return filtered navigation children of the curent folder
        """
        portal_catalog = self.portal.portal_catalog
        plone_portal_state = getMultiAdapter((self.context, self.request),
                name='plone_portal_state')
        sproperties = self.portal.portal_properties.get("slidernavigation_properties", None)
        if sproperties:
            bottom_level = sproperties.getProperty("bottom_level", 0)
            navigation_root_path = plone_portal_state.navigation_root_path()
            navigation_root = navigation_root_path.split("/")
            navigation_root_offset = len(navigation_root)
            current_context = self.context
            under_bottom_level = True
            while under_bottom_level:
                current_path = '/'.join(current_context.getPhysicalPath())
                current_level = len(current_path.split("/")) - navigation_root_offset
                if current_level <= bottom_level:
                    under_bottom_level = False
                else:
                    current_context = aq_parent(aq_inner(current_context))
            path = current_path
        else:
            current_path = '/'.join(self.context.getPhysicalPath())

        slidernavigation_source_path = self.context.getProperty("slidernavigation_source_path", None)
        if slidernavigation_source_path:
            path = slidernavigation_source_path
        else:
            path = current_path
        query={
            'path': {'query': path, 'depth':1},
            'portal_type': 'Folder',
            'sort_on': 'getObjPositionInParent'
        }
        results = portal_catalog(query)
        children = [child for child in results
                if not child.exclude_from_nav and not child.getPath() == path]
        return children

