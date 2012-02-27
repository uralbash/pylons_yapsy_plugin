"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController

from pylons import tmpl_context as c
from pylons.templating import render_jinja2 as render
from pylons_yapsy_plugin.model.meta import Session
from pylons_yapsy_plugin.lib import plugins

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        # Plugin uploads
        c.plugin_manager, c.deactivated_plugins = plugins.load_plugins()

        # Plugin menu uploads
        c.plugin_menu = []
        for plugin in c.plugin_manager.getPluginsOfCategory("Menu"):
            c.plugin_menu.append(plugin.plugin_object.get_html_menu())

        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()

