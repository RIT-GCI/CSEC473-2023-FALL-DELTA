from time import sleep
from nextcloud import NextCloud

def score_NextCloud(queue, alive, lock, url, port, value, team=0, username='User', password='Pass'):
    while alive():
        try:
            # may need to format url first with .format(os.environ['NEXTCLOUD_HOSTNAME'])
            nxc = NextCloud(endpoint=url, user=username, password=password)
            if nxc is not None:
                lock.acquire()
                queue.put({'service': 'NextCloud', 'status': 'UP', 'host' : url, 'value': value, 'team': team})
                lock.release()
            else:
                lock.acquire()
                queue.put({'service': 'NextCloud', 'status': 'DOWN', 'host' : url, 'value': value, 'team': team})
                lock.release()
        except Exception:
            lock.acquire()
            queue.put({'service': 'NextCloud', 'status': 'DOWN', 'host' : url, 'value': value, 'team': team})
            lock.release()
        sleep(300)