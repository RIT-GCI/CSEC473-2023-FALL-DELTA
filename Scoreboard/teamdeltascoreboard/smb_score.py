import smbclient
import smbprotocol
from time import sleep

USERNAME = "username"
PASSWORD = "password"

def score_SMB(queue, alive, lock, target, port, value, team=0):
    while alive():
        try:
            smbclient.register_session(target, USERNAME, PASSWORD)
            lock.acquire()
            queue.put({'service': 'SMB', 'status': 'UP', 'host' : target, 'value':value, 'team': team})
            lock.release()

        except smbprotocol.exceptions.SMBException:
            lock.acquire()
            queue.put({'service': 'SMB', 'status': 'UP', 'host' : target, 'value':value, 'team': team})
            lock.release()

        except Exception:
            lock.acquire()
            queue.put({'service': 'SMB', 'status': 'DOWN', 'host' : target, 'value':value, 'team': team})
            lock.release()
        sleep(300)