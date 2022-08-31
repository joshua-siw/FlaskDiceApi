# SimpleDiceFlask

Requirements: Python3, pip3, venv

Erstelle virtuelle Umgebung in SimpleDiceFlask
Windows
    cd *\virualenv
    python venv -m venv
    PowerShell
        .\Activate.ps1
    cmd.exe
        .\activate.bat

Installiere benötigte Pakete
    pip3 install -r requirements.txt

Anwendung starten

    in cmd.exe oder Powershell 
    
        "python3 wsgi.py"
	
Alternativ kann die Anwendung über uwsgi gestartet werden.

	"uwsgi --ini app.ini --need-app"
	

localhost:2784/api/dice aufrufen um zu würfeln.
	Antwort im Format: 
	
	"["number",2]"

localhost:2784/api/dicelist aufrufen um vorherige Ergebnisse anzuzeigen.
	Antwort im Format: 
	
	"["list",[2,3,1,5,2,4]]"

Platziere prometheus.yml in dein Prometheus verzeichniss oder füge folgende config hinzu.

- job_name: "dice"

    static_configs:
      - targets: ["localhost:2784"]
      # use with uwsgi
      #- targets: ["localhost:6800"]

Prometheus Metriken werden über den Port 9090 ausgegeben
und sind mit 
- 'count_throws'
- 'show_results'
verfügbar


Diese "Api" verwendet flask_session welche Cookies zur authentifizierung benötigen, um zwischen den unregistrierten Usern zu unterscheiden.




