import dns.message, dns.query
from time import sleep

DPORT = 53 # UDP

def score_DNS(queue, alive, lock, target, _, value, team=0, target_port=DPORT):
    query = dns.message.make_query(".", dns.rdatatype.NS, flags=0) # Create a query to 

    while alive():
        try:
            res = dns.query.udp(query, target, timeout=10)
            if res.answer is not None:
                lock.acquire()
                queue.put({'service': 'dns', 'status': 'UP', 'host' : target, 'value':value, 'team': team})
                lock.release()
            else:
                lock.acquire()
                queue.put({'service': 'dns', 'status': 'DOWN', 'host' : target, 'value':value, 'team': team})
                lock.release()
        except Exception:
            lock.acquire()
            queue.put({'service': 'dns', 'status': 'DOWN', 'host' : target, 'value':value, 'team': team})
            lock.release()
        sleep(300)