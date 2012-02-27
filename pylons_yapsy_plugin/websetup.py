"""Setup the pylons_yapsy_plugin application"""
import logging

from pylons_yapsy_plugin.config.environment import load_environment
from pylons_yapsy_plugin.model.meta import Session, Base
from pylons_yapsy_plugin.model import *

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup pylons_yapsy_plugin here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)
