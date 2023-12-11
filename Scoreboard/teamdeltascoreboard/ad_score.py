# import ldap
# from time import sleep

# def score_AD(queue, alive, lock, servername, port, value=1, team=0):
#     while alive():
#         try:
#             l = ldap.initialize('ldap://192.168.2.3')
#             l.simple_bind_s()

#             l.search('(&(objectCategory=person)(objectClass=user))', ldap.SCOPE_SUBTREE)
#             lock.acquire()
#             queue.put({'service': 'Active Directory', 'status': 'UP', 'host' : servername, 'value': value, 'team': team})
#             lock.release()

#         except Exception:
#             lock.acquire()
#             queue.put({'service': 'Active Directory', 'status': 'DOWN', 'host' : servername, 'value': value, 'team': team})
#             lock.release()
#         sleep(60)

import pyad.adquery
import pyad.pyadutils

# Define the LDAP server to check (replace with your server's IP or hostname)
ldap_server = "ldap://192.168.2.150"

def score_AD(queue, alive, lock, servername, port, value=1, team=0):
    try:
        # Create an AD query object with the LDAP server
        pyad.pyadutils.adldap_set(ldap_server)
        q = pyad.adquery.ADQuery()

        # Attempt a simple query to check if AD is responsive
        q.execute_query(attributes=["distinguishedName"], where_clause="objectClass='*'", base_dn="")

        # If the query is successful, AD is running and responsive
        lock.acquire()
        queue.put({'service': 'Active Directory', 'status': 'UP', 'host' : servername, 'value': value, 'team': team})
        lock.release()
        return True

    except Exception as e:
        lock.acquire()
        queue.put({'service': 'Active Directory', 'status': 'DOWN', 'host' : servername, 'value': value, 'team': team})
        lock.release()

