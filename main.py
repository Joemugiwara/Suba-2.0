# -*- coding: utf-8 -*-
"""
SUBA 2.0 — version Android (Kivy)
Catégories modifiables (ajout / suppression) avec listes d'étudiants indépendantes.
Données sauvegardées dans le dossier privé de l'appli (suba_data.json).
"""
import json
import os

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex as hexc
from kivy.utils import escape_markup

# ----------------------------------------------------------------------
# Réglages
# ----------------------------------------------------------------------
TITLE = "SUBA 2.0"
SUBTITLE = "Masta na nga suba ndege olingi subasement ne tombera jamais."

DEFAULT_CATEGORIES = [
    "Projet tutoré",
    "Pratique professionnelle",
    "Rapport de stage",
    "Vaseline",
]
