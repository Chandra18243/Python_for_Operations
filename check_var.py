import psutil
import subprocess

usage = psutil.disk_usage('/var')

if usage.percent > 60:
    print(f"/var usage is {usage.percent}%, cleaning YUM cache...")
    subprocess.run(['yum', 'clean', 'all'])
else:
    print(f"/var usage is {usage.percent}%, no action needed.")


#Add it to crontab if you want to run daily
#0 3 * * * /usr/bin/python3 /opt/linux/lifecycle/check_var.py >> /var/log/lifecycle.log 2>&1
