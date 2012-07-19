import unittest2 as unittest

#from zope.component import getMultiAdapter
from zope import interface

from plone.app.testing import TEST_USER_ID, setRoles

from collective.slidernavigation.viewlet import SliderNavigation
from collective.slidernavigation.interfaces import ISliderNavigation
from collective.slidernavigation.testing import \
   COLLECTIVE_SLIDERNAVIGATION_INTEGRATION_TESTING


class TestSlidernavigationViewlet(unittest.TestCase):
    layer = COLLECTIVE_SLIDERNAVIGATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        interface.alsoProvides(self.portal.REQUEST, ISliderNavigation)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        self.portal.invokeFactory('Folder', 'test-folder')
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('Link', 'link1')

        self.folder.invokeFactory('Folder', 'subfolder1')
        self.subfolder1 = self.folder['subfolder1']
        self.subfolder1.invokeFactory('Folder', 'subsubfolder1')
        self.subfolder1.invokeFactory('Folder', 'subsubfolder2')
        self.subfolder1.invokeFactory('Folder', 'subsubfolder3')

        self.folder.invokeFactory('Folder', 'subfolder2')
        self.subfolder2 = self.folder['subfolder2']



    def test_viewlet_tabs(self):
        self.context = self.folder
        viewlet = SliderNavigation(self.context, self.request, None, None)
        viewlet.update()
        # there should be two tabs
        self.assertTrue(len(viewlet.get_children()) == 2, "folder should have 2 children")



def test_suite():
        return unittest.defaultTestLoader.loadTestsFromName(__name__)
