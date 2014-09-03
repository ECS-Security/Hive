__author__ = 'Maskonk'

from pyad import *


pyad.pyad_setdefaults(ldap_server="ldap://10.1.63.2", username="automated", password="Arugula01")
user = pyad.aduser.ADUser.from_cn("Test")

#ou = pyad.adcontainer.ADContainer.from_dn("ou=workstations, dc=domain, dc=com")
#computer = pyad.adcomputer.ADComputer.create("Test", ou)
