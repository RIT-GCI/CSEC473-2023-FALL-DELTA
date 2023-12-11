from icmplib import ping
from time import sleep


def score_ICMP(queue, alive, lock, target, value, team=0):
    while alive():
        try:
            host = ping(target, privileged=False)

            if host.is_alive: # Is alive === reachable
                lock.acquire()
                queue.put({'service': 'icmp', 'status': 'UP', 'host' : target, 'value':value, 'team': team}) 
                lock.release()
            else:
                lock.acquire()
                queue.put({'service': 'icmp', 'status': 'DOWN', 'host' : target, 'value':value, 'team': team})
                lock.release()

        except Exception: # I don't think this is reachable, but just in case.
            lock.acquire()
            queue.put({'service': 'icmp', 'status': 'DOWN', 'host' : target, 'value':value, 'team': team})
            lock.release()
        sleep(300)