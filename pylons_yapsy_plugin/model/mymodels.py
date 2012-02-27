from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import String, Unicode, UnicodeText, Integer, DateTime,\
                             Boolean, Float
from sqlalchemy.orm import relation, backref, synonym

from pylons_yapsy_plugin.model.meta import Base

class DeactivatedPlugins(Base):
    """Status of loaded plugin.
    """
    __tablename__ = 'deactivated_plugins'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(50), unique=True)

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return "%s" % self.name

