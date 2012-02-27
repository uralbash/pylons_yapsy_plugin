from pylons_yapsy_plugin.tests import *

class TestPluginController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='plugin', action='index'))
        # Test response...
