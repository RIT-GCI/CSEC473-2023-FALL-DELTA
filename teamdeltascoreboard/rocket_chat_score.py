from rocketchat_API.rocketchat import RocketChat
import rocketchat_API
from time import sleep


def score_rocket_chat(queue, alive, lock, server, port, value, team=0):
    while alive():
        try:
            rocket = RocketChat('Username', 'Password', server_url='http://'+server)
            
            lock.acquire()
            queue.put({'service': 'RocketChat', 'status': 'UP', 'host':server, 'value':value, 'team': team})
            lock.release()

        except rocketchat_API.APIExceptions.RocketExceptions.RocketAuthenticationException:
            lock.acquire()
            queue.put({'service': 'RocketChat', 'status': 'UP', 'host':server, 'value':value, 'team': team})
            lock.release()
        except:
            lock.acquire()
            queue.put({'service': 'RocketChat', 'status': 'DOWN', 'host':server, 'value':value, 'team': team})
            lock.release()
        sleep(300)