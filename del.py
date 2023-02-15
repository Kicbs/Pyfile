import os
import ctypes
def get_firewall_logs():
    #logs=os.popen("cd C:\WINDOWS\system32\LogFiles\Firewall").read()
    print('hello')
    logs=os.popen("type C:\WINDOWS\system32\LogFiles\Firewall\pfirewall.log").read()
    logs=logs.splitlines()
    log_list=[]
    for log in logs:
        log=log.strip()
        if log:
            log_list.append(log)
    return log_list
firewall_log=get_firewall_logs()
print(firewall_log)