from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig

class CollectiveSlidernavigation(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # load zcml
        import collective.slidernavigation
        xmlconfig.file('configure.zcml',
                collective.slidernavigation,
                context=configurationContext)

    def setUpPloneSite(self, portal):
        # install into plone using portal_setup
        applyProfile(portal, 'collective.contentleadimage:default')
        applyProfile(portal, 'collective.slidernavigation:default')


COLLECTIVE_SLIDERNAVIGATION_FIXTURE = CollectiveSlidernavigation()
COLLECTIVE_SLIDERNAVIGATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SLIDERNAVIGATION_FIXTURE,),
    name="CollectiveSlidernavigation:Integration")
COLLECTIVE_SLIDERNAVIGATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SLIDERNAVIGATION_FIXTURE,),
    name="CollectiveSlidernavigation:Functional")
