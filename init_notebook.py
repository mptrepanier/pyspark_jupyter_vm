#!/usr/bin/env python

import os
import json
from subprocess import call, Popen, PIPE


# additional packages to install
pkgs = [
    'lxml',
    'jupyter-spark',
    'jgscm'
]

# use pip to install packages
for pkg in pkgs:
    call('/home/anaconda2/bin/pip install {}'.format(pkg), shell=True)

# create Jupyter configuration file
call('mkdir -p /home/anaconda2/etc/jupyter/', shell=True)
with open('/home/anaconda2/etc/jupyter/jupyter_notebook_config.py', 'w') as f:
    opts = [
	    'c.Application.log_level = "DEBUG"',
	    'c.NotebookApp.ip = "0.0.0.0"',
	    'c.NotebookApp.open_browser = False',
	    'c.NotebookApp.port = 8888',
	    'c.NotebookApp.token = ""',
    ]
    f.write('\n'.join(opts) + '\n')

# create kernel spec file
kernel = {
    'argv': [
        '/home/anaconda2/bin/python',
        '-m',
        'ipykernel',
        '-f',
        '{connection_file}'
    ],
    'display_name': 'PySpark',
    'language': 'python',
    'env': {
        'PYTHONHASHSEED': '0',
        'SPARK_HOME': '/usr/lib/spark/',
        'PYTHONPATH': '/usr/lib/spark/python/:/usr/lib/spark/python/lib/py4j-0.10.3-src.zip'
    }
}

call('mkdir -p /home/anaconda2/share/jupyter/kernels/pyspark/', shell=True)
with open('/home/anaconda2/share/jupyter/kernels/pyspark/kernel.json', 'w') as f:
	json.dump(kernel, f)

# setup jupyter-spark extension
call('/home/anaconda2/bin/jupyter serverextension enable --user --py jupyter_spark', shell=True)
call('/home/anaconda2/bin/jupyter nbextension install --user --py jupyter_spark', shell=True)
call('/home/anaconda2/bin/jupyter nbextension enable --user --py jupyter_spark', shell=True)
call('/home/anaconda2/bin/jupyter nbextension enable --user --py widgetsnbextension', shell=True)

# create systemd service file for Jupyter notebook server process
call ('mkdir /vagrant/notebooks', shell=True)
with open('/lib/systemd/system/jupyter.service', 'w') as f:
	opts = [
		'[Unit]',
		'Description=Jupyter Notebook',
		# 'After=hadoop-yarn-resourcemanager.service',
		'[Service]',
		'Type=simple',
		'User=root',
		'Group=root',
		'WorkingDirectory=/vagrant/notebooks/',
        'ExecStart=/home/anaconda2/bin/python /home/anaconda2/bin/jupyter notebook',
		'Restart=always',
		'RestartSec=1',
		'[Install]',
		'WantedBy=multi-user.target'
	]
	f.write('\n'.join(opts) + '\n')

# add Jupyter service to autorun and start it
call('systemctl daemon-reload', shell=True)
call('systemctl enable jupyter', shell=True)
call('service jupyter start', shell=True)

# give all permissions to Anaconda directory
call('chmod -R 777 /home/anaconda2/', shell=True)