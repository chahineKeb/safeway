import sys
import os

# Indique le dossier de l'application
sys.path.insert(0, os.path.dirname(__file__))

# "app" = nom du fichier app.py, "app" = l'objet Flask dedans
from app import app as application
