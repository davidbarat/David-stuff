[Unit]
Description=Gunicorn Agent
After=network.target

[Service]
WorkingDirectory=/applis/elk
Environmen="PATH=/applis/elk/flask/bin"
ExecStart=/applis/elk/flask/bin/gunicorn --workers 3 --bind unix:mysite.sock -m 660 wsgi:app

[install]
WantedBy=multi-user.target