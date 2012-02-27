import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylons_yapsy_plugin.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AboutController(BaseController):

    def index(self):

        return render('/plugin/menu/about/index.html')
