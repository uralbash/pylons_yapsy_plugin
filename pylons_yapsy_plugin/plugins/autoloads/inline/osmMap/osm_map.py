# coding=utf-8
import datetime

from pylons import request, response, session, tmpl_context as c, url
from pylons_yapsy_plugin.lib.base import render
from pylons_yapsy_plugin.plugins.categories import inline

class osm_map_plugin(inline.Inline):
    """ Show OpenStreetMap
    """
    name = 'Open Street Map'

    def init_plugin(self):
        print "--> initialization osm_map plugin..."
        return "--> complete install osm_map"

    def get_html_features(self):
        return render('plugin/inline/osm_map.html')

    def update(self, equipment_id):
        pass

    def get_style(self):
        return ''

    def get_onload(self):
        return '''GetMap();
        removeElement('OpenLayers.Control.Attribution_7');'''

