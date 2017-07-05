import js2py
import json

#On transforme le fichier js en fichier python avec la bibliothèque js2py
js2py.translate_file("cascade.js", "cascade.py")

#On importe la bibliothèque python créée
from cascade import cascade

#On lit le fichier geojson
with open("polygon.geojson") as json_data:
	polygone = json.load(json_data)

#On récupère le paramètre "geometry" du geojson
geometry = polygone['features'][0]['geometry']

#On appelle la méthode de cascade nous donnant toutes les tuiles
cascade.tilesForEveryZoom(geometry)
