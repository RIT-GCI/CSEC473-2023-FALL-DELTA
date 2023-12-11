import pyodbc
from time import sleep

DDATABASE='localhost'

def score_SQL(queue, alive, lock, server, value, team=0, database=DDATABASE):
    while alive():
        try:
            pyodbc.connect('Driver{SQL Server};'
                           f'Server={server},3306;'
                           f'Database={database};'
                           'Trusted_Connection=yes;'
                           'Timeout=5;')
            
            # SQL Server connects sucessfully 
            lock.aquire()
            queue.put({'service': 'sql', 'status': 'UP', 'host':server, 'value':value, 'team': team})
            lock.release()

        # SQL Server failed to respond
        except:
            lock.acquire()
            queue.put({'service': 'sql', 'status': 'DOWN', 'host':server, 'value':value, 'team': team})
            lock.release()
        sleep(300)