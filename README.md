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

Api starten
    in cmd.exe oder Powershell 
        python3 wsgi.py
Alternativ kann die Anwendung über uwsgi gestartet werden
	

localhost:2784/api/dice aufrufen um zu würfeln.
	Antwort im Format: 
localhost:2784/api/dicelist aufrufen um vorherige Ergebnisse anzuzeigen.

Place prometheus.yml where you execute Prometheus or add to your scraperconfig from prometheus.txt
Platziere prometheus.yml in dein Prometheus verzeichniss oder füge folgende config hinzu.

- job_name: "dice"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:2784"]
      # use with uwsgi
      #- targets: ["localhost:6800/api"]

Diese "Api" verwendet flask session objekte welche cookies als authentifizierung benötigen.



