__author__ = 'Maskonk'

from pyad import pyad_setdefaults
from pyad import aduser

#This is the pyad version
#setdefaults is supposed to direct it to the AD and log it in but it is not able to find it remotly
#Since setdefaults is supposed to not be required if you are connected to an AD
# it may be possible to get this working while connected to the AD

pyad_setdefaults(ldap_server="DevOps.internal", username="automated", password="Arugula01")
user = aduser.ADUser.from_cn("Test")

#ou = pyad.adcontainer.ADContainer.from_dn("ou=workstations, dc=domain, dc=com")
#computer = pyad.adcomputer.ADComputer.create("Test", ou)
