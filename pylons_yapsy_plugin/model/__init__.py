"""The application's model objects"""
from pylons_yapsy_plugin.model.meta import Session, Base
from pylons_yapsy_plugin.model.mymodels import *


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

