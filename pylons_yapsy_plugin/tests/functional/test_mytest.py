from pylons_yapsy_plugin.tests import *

class TestMytestController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='mytest', action='index'))
        # Test response...
