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
        self.autoplay = False
        self.interval = None
        self.fade_in_speed = None
        self.fade_out_speed = None
        self.effect = None
        self.base_url = self.portal.portal_url()
        self.cpath = '/'.join(self.context.getPhysicalPath())
        self.nav_source_context = None
        self.children = self.get_children()

    def get_children(self):
        """ return filtered navigation children of the curent folder
        """
        portal_catalog = self.portal.portal_catalog
        plone_portal_state = getMultiAdapter((self.context, self.request),
                name='plone_portal_state')
        plone_context_state = getMultiAdapter((self.context, self.request),
                name='plone_context_state')
        sproperties = self.portal.portal_properties.get("slidernavigation_properties", None)
        current_context = plone_context_state.folder()
        if sproperties:
            bottom_level = sproperties.getProperty("bottom_level", 0)
            navigation_root_path = plone_portal_state.navigation_root_path()
            navigation_root = navigation_root_path.split("/")
            navigation_root_offset = len(navigation_root)
            under_bottom_level = True
            while under_bottom_level:
                current_path = '/'.join(current_context.getPhysicalPath())
                current_level = len(current_path.split("/")) - navigation_root_offset
                if current_level <= bottom_level:
                    under_bottom_level = False
                else:
                    current_context = aq_parent(aq_inner(current_context))
            path = current_path
            self.nav_source_context = current_context
        else:
            current_path = '/'.join(current_context.getPhysicalPath())
            self.nav_source_context = current_context

        slidernavigation_source_path = self.context.getProperty("slidernavigation_source_path", None)
        autoplay = self.context.getProperty("slidernavigation_autoplay", False)
        if autoplay:
            self.autoplay = 'true'
        else:
            self.autoplay = 'false'
        self.interval = self.context.getProperty("slidernavigation_interval", 3000)
        self.fade_in_speed = self.context.getProperty("slidernavigation_fadeinspeed", 500)
        self.fade_out_speed = self.context.getProperty("slidernavigation_fadeoutspeed", 1000)
        self.effect = self.context.getProperty("slidernavigation_effect", 'default')

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
                if not child.exclude_from_nav]
        return children

