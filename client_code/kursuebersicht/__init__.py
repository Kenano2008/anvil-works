from ._anvil_designer import kursuebersichtTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class kursuebersicht(kursuebersichtTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.repeating_panel_1.items = anvil.server.call('get_kurse')