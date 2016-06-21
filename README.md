**Dieses Repository basiert auf einer alten Version von OParl und
wird nicht mehr weiter entwickelt. Es verbleibt jedoch aus Gründen
der Nachvollziehbarkeit auf GitHub.**

----

Eine serverseitige Referenz-Implementierung der OParl API mit Beispieldaten.

Dieser Server kann als Gegenstück für die Entwicklung des [Validierungs-Clients](https://github.com/OParl/validator) genutzt werden.

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

Die Implementierung des Servers ist in der Datei [server.py](https://github.com/OParl/reference-server/blob/master/server.py) enthalten und basiert auf dem [Flask](http://flask.pocoo.org/) Framework.

Die Beispieldaten sind in Form der JSON-Datei [data.json](https://github.com/OParl/reference-server/blob/master/data.json) enthalten. Alle URls, die sich auf das Referenz-System beziehen, verwenden den Hostnamen "127.0.0.1:5000". Für die öffentliche Instanz wird dies automatisch in "refserv.oparl.de" umgewandelt.
