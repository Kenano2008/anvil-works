from ._anvil_designer import RowTemplate1Template
from anvil import *
from ..anmeldung import anmeldung


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_kurs.text = self.item['bezeichnung']
    self.label_wochentag.text = self.item['wochentag']
    self.label_trainer.text = self.item['trainer']
    self.label_teilnehmer.text = str(self.item['teilnehmer'])

  @handle("button_anmelden", "click")
  def button_anmelden_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    form.content_panel.add_component(anmeldung(self.item))