# coding=utf-8
from pylons import request, response, session, tmpl_context as c, url
from pylons_yapsy_plugin.lib.base import render
from pylons_yapsy_plugin.plugins.categories import menu
from pylons_yapsy_plugin.model.meta import Session as s

class about_plugin(menu.Menu):
    """ About plugin
    """
    name = 'About plugin'

    def init_plugin(self):
        print "--> initialization About plugin..."
        return "--> complete install About"

    def get_html_menu(self):
        return render('/plugin/menu/about/menu.html')

    def get_style(self):
        return ''

    def get_onload(self):
        return ''

