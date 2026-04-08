import anvil.server
import sqlite3
from anvil.files import data_files

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


def get_connection_dict():
  conn = sqlite3.connect(data_files["Pipic_Kenan_fitnessstudio.db"])
  conn.row_factory = sqlite3.Row
  return conn
  
@anvil.server.callable
def get_kurse():
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        k.KID AS kid,
        k.Bezeichnung AS bezeichnung,
        k.Wochentag AS wochentag,
        k.Uhrzeit AS uhrzeit,
        t.Vorname || ' ' || t.Nachname AS trainer,
        k.MaxTeilnehmeranzahl AS max_teilnehmer,
        COUNT(a.MID) AS teilnehmer
      FROM Kurs k
      JOIN Trainer t ON k.TID = t.TID
      LEFT JOIN anmelden a ON k.KID = a.KID
      GROUP BY
        k.KID,
        k.Bezeichnung,
        k.Wochentag,
        k.Uhrzeit,
        t.Vorname,
        t.Nachname,
        k.MaxTeilnehmeranzahl
      ORDER BY k.Wochentag, k.Uhrzeit
    """).fetchall()

  return [dict(row) for row in result]

