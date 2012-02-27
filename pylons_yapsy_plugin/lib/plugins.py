# coding=utf8
import pylons

from yapsy.PluginManager import PluginManager

from pylons_yapsy_plugin.plugins.categories import menu, inline
from pylons_yapsy_plugin.model.meta import Session as s
from pylons_yapsy_plugin.model.mymodels import DeactivatedPlugins
from pylons_yapsy_plugin.model import meta

def load_plugins():
    """ Load plugin for environment. See lib/base.py
    """
    # Create plugin manager
    manager = PluginManager()
    # Tell it the default place(s) where to find plugins
    manager.setPluginPlaces(["pylons_yapsy_plugin/plugins/"])
    # Define the various categories corresponding to the different
    # kinds of plugins you have defined
    manager.setCategoriesFilter({
        "Menu" : menu.Menu,
        "Inline" : inline.Inline,
        })

    manager.locatePlugins()

    # Deactivate plugin
    # Список деактивированных плагинов из БД
    deactivatedPlugins = [plugin.name for plugin in\
            s.query(DeactivatedPlugins).all()]

    # Список кандидатов на загрузку
    candidates = manager.getPluginCandidates()
    # Список деактивированных плагинов в формате yapsy
    deactivatedList = []

    for candidate in candidates:
        if candidate[2].name in deactivatedPlugins:
            deactivatedList.append(candidate)

    # Исключаем плагины которые указанны в БД
    for plugin in deactivatedList:
        manager.removePluginCandidate(plugin)

    # Load plugins
    manager.loadPlugins()

    return manager, [plugin[2] for plugin in deactivatedList]

