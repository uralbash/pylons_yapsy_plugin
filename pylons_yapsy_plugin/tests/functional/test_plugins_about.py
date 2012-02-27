from pylons_yapsy_plugin.tests import *

class TestAboutController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='plugins/about', action='index'))
        # Test response...
