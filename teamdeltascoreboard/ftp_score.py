from ftplib import FTP, error_perm
from time import sleep

DUSERNAME = 'grey_admin'
DPASSWORD = '10Grey_infra_rocks:'
DPORT = 21

def score_FTP(queue, alive, lock, target, port=DPORT, value=1, team=0, username=DUSERNAME, password=DPASSWORD):
    while alive():
        try:
        
            ftp = FTP(target)
            ftp.login()
            ftp.quit()
            
            # FTP Server connects sucessfully 
            lock.acquire()
            queue.put({'service': 'FTP', 'status': 'UP', 'host':target, 'value':value, 'team': team})
            lock.release()
        except error_perm:
            queue.put({'service': 'FTP', 'status': 'UP', 'host':target, 'value':value, 'team': team})
        # FTP Server failed to respond
        except:
            lock.acquire()
            queue.put({'service': 'FTP', 'status': 'DOWN', 'host':target, 'value':value, 'team': team})
            lock.release()
        sleep(300)
