import ldap

#connection = wmi.WMI("10.1.63.2", user="automated", password="Arugula01")
#print("connection is establised")

#pyad.pyad_setdefaults(ldap_server=wmi.WMI("10.1.63.2", user="automated", password="Arugula01"))
#user1 = pyad.aduser.ADUser.from_cn("Test")

try:
    l = ldap.open("ldap://10.1.63.2")
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)
    bind = l.simple_bind_s("automated", "Arugula01")
    print("here")
except ldap.LDAPError, e:
    print e

try:
    dn = "cn=replica,dc=example,dc=com"
    attrs = {}
    attrs['objectclass'] = ['top', 'Test', 'simpleSecurityObject']
    attrs['cn'] = 'Tester'
    attrs['userPassword'] = '@pp1es'
    attrs['description'] = 'User object for replication using slurpd'
    ldif = ldap.modlist.addModlist(attrs)
    l.add_s(dn, ldif)
    l.unbind_s()
except ldap.LDAPError, e:
    print e