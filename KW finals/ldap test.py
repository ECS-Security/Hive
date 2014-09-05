import ldap
from ldap import modlist
import wmi
import pyad

#Both the WMI and LDAP connections here work
#But neither the add user or the list users work for either pyad or LDAP


#WMI connection
connection = wmi.WMI("10.1.63.2", user="automated", password="Arugula01")
print("Connection is established")


#LDAP connection
l = open("10.1.63.2")
l.protocol_version = ldap.VERSION3
l.set_option(ldap.OPT_REFERRALS, 0)
bind = l.simple_bind_s("automated", "Arugula01")

#To add a user via pyad
pyad.pyad_setdefaults(ldap_server=wmi.WMI("10.1.63.2", user="automated", password="Arugula01"))
#user1 = pyad.aduser.ADUser.from_cn("Test")

#To add a user via LDAP (Does not work at the moment.)
try:
    dn = "cn=Tester, dc=DevOps, dc=internal"
    attrs = {}
    attrs['objectclass'] = ['top', 'Test', 'simpleSecurityObject']
    attrs['cn'] = 'Tester'
    attrs['userPassword'] = '@pp1es'
    attrs['description'] = 'User object for replication using slurpd'
    ldif = modlist.addModlist(attrs)
    l.add_s(dn, ldif)
    l.unbind_s()
except ldap.LDAPError, e:
    print e


#To list all the users via LDAP (Does not work at the moment.)
baseDN = "ou=Tester, ou=Testers"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None
searchFilter = "cn=b*"

try:
    ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
    print(ldap_result_id)
    result_set = []
    while 1:
        result_type, result_data = l.result(ldap_result_id, 0)
        if result_data == []:
            print("None")
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    print result_set
except ldap.LDAPError, e:
    print("Error")
    print e