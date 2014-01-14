OParl Referenz-Server
=====================

Eine serverseitige Referenz-Implementierung der OParl API mit Beispieldaten.

Dieser Server kann als Gegenstück für die Entwicklung des Validierungs-Clients genutzt werden.

## Status

Der Reference Server ist nicht auf dem gleichen Stand wie die Spezifikation.

Sobald die Sepzifikation 1.0 verabschieded ist, kann der Code daran angepasst werden.

## Installation

### Zusammenfassung

	mkdir OParl
	cd OParl
    git clone https://github.com/OParl/reference-server.git
    cd reference-server
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python server.py

Der Aufruf des Servers erfolgt über die URL http://127.0.0.1:5000/

### Systemvoraussetzungen

Es wird Python 2.7, git, virtualenv und pip benötigt.

## Entwicklung

Die Implementierung des Servers ist in der Datei "server.py" enthalten und basiert auf dem Flask Framework.

Die Beispieldaten sind in Form der JSON-Datei "data.json" enthalten.
