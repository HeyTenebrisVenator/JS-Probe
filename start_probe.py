import os


open('/usr/bin/probe_for_js', 'w').write(open('Modules/probe', 'r').read())
open('/usr/lib/systemd/system/js_probe.service', 'w').write(open('Modules/job', 'r').read())

print('reloading daemon')
os.system('sudo systemctl daemon-reload')

print('Starting script...')
os.system('sudo systemctl start js_probe.service')
os.system('sudo systemctl enable js_probe.service')
os.system('sudo systemctl restart js_probe.service')