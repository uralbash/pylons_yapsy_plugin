import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylons_yapsy_plugin.lib.base import BaseController, render
from pylons_yapsy_plugin.model.meta import Session as s
from pylons_yapsy_plugin.model.mymodels import DeactivatedPlugins

log = logging.getLogger(__name__)

class PluginController(BaseController):

    def getIdByName(self, name=''):
        id = s.query(DeactivatedPlugins.id).\
                    filter(DeactivatedPlugins.name==name).first()
        return id[0]

    def index(self, format='html'):
        c.plugins = []

        for plugin in c.plugin_manager.getAllPlugins():
            c.plugins.append(plugin)

        c.plugins = sorted(c.plugins + c.deactivated_plugins,
                key=lambda plugin: plugin.name)

        c.getIdByName = self.getIdByName

        return render('/plugin/index.html')

    def create(self):
        new_deactivated = DeactivatedPlugins()
        new_deactivated.name = request.GET['name']
        s.add(new_deactivated)
        s.commit()

        c.http_referer = str(request.environ.get('HTTP_REFERER', ''))\
                         or str(request.params.get('came_from', ''))\
                         or url('/')
        redirect(url(c.http_referer))

    def delete(self, id):
        plugin = s.query(DeactivatedPlugins).\
                filter(DeactivatedPlugins.id == id).first()
        s.delete(plugin)
        s.commit()

        c.http_referer = str(request.environ.get('HTTP_REFERER', ''))\
                         or str(request.params.get('came_from', ''))\
                         or url('/')
        redirect(url(c.http_referer))

