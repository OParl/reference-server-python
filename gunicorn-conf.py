workers = 1
bind = '127.0.0.1:5002'
accesslog = '/home/oparl/logs/gunicorn/refserv.access.log'
errorlog = '/home/oparl/logs/gunicorn/refserv.error.log'
proc_name = 'refserv'
loglevel = 'info'
