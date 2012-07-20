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
        self.base_url = self.portal.portal_url()
        self.cpath = '/'.join(self.context.getPhysicalPath())

        sn_properties = self.get_sn_properties()
        self.bottom_level = sn_properties['bottom_level']

        sn_cproperties = self.get_sn_cproperties()
        self.sn_source_path = sn_cproperties['sn_source_path']
        self.autoplay = sn_cproperties['autoplay']
        self.interval = sn_cproperties['interval']
        self.fade_in_speed = sn_cproperties['fade_in_speed']
        self.fade_out_speed = sn_cproperties['fade_out_speed']
        self.effect = sn_cproperties['effect']

        self.nav_source_context = self.get_nav_source_context()
        self.children = self.get_children()
        self.initial_pane_content = self.get_initial_pane_content()


    def get_initial_pane_content(self):
        """ return inital rendered pane content
        """
        pane_content_view = getMultiAdapter((self.context,
            self.request), name=u"pane_content")
        #pane_content_view = self.portal.unrestrictedTraverse('@@pane_content')
        if len(self.children):
            initial_pane_content = pane_content_view.__call__(self.children[0]['UID'])
        else:
            initial_pane_content = pane_content_view.__call__(self.context.UID())
        return initial_pane_content

    def get_sn_properties(self):
        """ return slidernavigation properties from:
            portal_properties/slidernavigation_properties
            return: {'bottom_level': bottom_level}
        """
        properties = {}
        plone_tools = getMultiAdapter((self.context, self.request),
                name='plone_tools')
        pproperties = plone_tools.properties()
        sn_properties = pproperties.get("slidernavigation_properties", None)
        if not sn_properties:
            return
        properties['bottom_level'] = sn_properties.getProperty("bottom_level", 0)
        return properties

    def get_sn_cproperties(self):
        """ return slidernavigation from context
            return: {
                'sn_source_path': sn_source_path,
                'autoplay': autoplay
            }
        """
        cproperties = {}
        cproperties['sn_source_path'] = \
                self.context.getProperty("sn_source_path", None)
        autoplay = self.context.getProperty("slidernavigation_autoplay", False)
        if autoplay:
            cproperties['autoplay'] = 1
        else:
            cproperties['autoplay'] = 0
        cproperties['interval'] = \
                self.context.getProperty("slidernavigation_interval", 3000)
        cproperties['fade_in_speed'] = \
                self.context.getProperty("slidernavigation_fadeinspeed", 500)
        cproperties['fade_out_speed'] = \
                self.context.getProperty("slidernavigation_fadeoutspeed", 1000)
        cproperties['effect'] = \
                self.context.getProperty("slidernavigation_effect", 'default')
        return cproperties

    def get_nav_source_context(self):
        """ return current context object but respect self.bottom_level
        """
        plone_portal_state = getMultiAdapter((self.context, self.request),
                name='plone_portal_state')
        plone_context_state = getMultiAdapter((self.context, self.request),
                name='plone_context_state')
        current_context = plone_context_state.folder()
        if self.bottom_level:
            navigation_root_path = plone_portal_state.navigation_root_path()
            navigation_root = navigation_root_path.split("/")
            navigation_root_offset = len(navigation_root)
            under_bottom_level = True
            while under_bottom_level:
                current_path = '/'.join(current_context.getPhysicalPath())
                current_level = len(current_path.split("/")) - navigation_root_offset
                if current_level <= self.bottom_level:
                    under_bottom_level = False
                else:
                    current_context = aq_parent(aq_inner(current_context))
        return current_context

    def get_children(self):
        """ return filtered children braines of self.sn_source_path
            if is set or nav_source_path
        """
        portal_catalog = self.portal.portal_catalog
        nav_source_path = '/'.join(self.nav_source_context.getPhysicalPath())
        if self.sn_source_path:
            path = self.sn_source_path
        else:
            path = nav_source_path
        query={
            'path': {'query': path, 'depth':1},
            'portal_type': 'Folder',
            'sort_on': 'getObjPositionInParent'
        }
        results = portal_catalog(query)
        children = [child for child in results
                if not child.exclude_from_nav]
        return children

