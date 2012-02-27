import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylons_yapsy_plugin.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MytestController(BaseController):

    def index(self):

        c.plugin_address = []
        c.styles = []
        c.onload = []
        for plugin in c.plugin_manager.getPluginsOfCategory("Inline"):
            c.plugin_address.append(plugin.\
                    plugin_object.get_html_features())
            c.styles.append(plugin.plugin_object.get_style())
            c.onload.append(plugin.plugin_object.get_onload())

        return render('/mytest.html')

