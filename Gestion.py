#!/usr/bin/python
import sys
from snimpy.manager import Manager as M
from snimpy.manager import load
import argparse #Para la gestion de los argumentos de entrada

def setter(m):
	f = open(archivo, 'r')
	for line in f:
		a=line.split()
		if (a):
			#print(a)
			print("Valor Anterior de ", a[0], getattr(m, a[0], a[1]))
			setattr(m, a[0], a[1])

def checker(m):
	f = open(archivo, 'r')
	for line in f:
		a=line.split()
		if (a):
			print("Valor buscado",a[0] ," = ", a[1])
			if (a[1]==getattr(m, a[0])):
				print("Correcto")

ip="10.10.10.2"
archivo='configuracion.ini'
check=False

#Anterior gestion de los argumentos de entrada
# if (len(sys.argv)>1):
# 	for x in sys.argv:
# 		if ("check" in x.islower()):
# 		check=True

# if (len(sys.argv)==2):
# 	ip=sys.argv[1]

# if (len(sys.argv)>3):
# 	ip=sys.argv[1]
# 	archivo=sys.argv[2]

#Nueva gestion de los argumentos de entrada
parser = argparse.ArgumentParser(description='Realiza gets y sets SNMP leyendo un archivo en el que se le indican pares de OIDs y valores')
parser.add_argument('--ip',action='store',type=str, metavar='IP', default="10.10.10.2",
					help='Direccion IP del agente SNMP')
parser.add_argument('--f',action='store',type=str,default='configuracion.ini',help='archivo de configuracion')
parser.add_argument('--check',action='store_const',const=True)
args = parser.parse_args()
if (args.check):
	print("only checking, not setting")

load("mibs/RFC1155-SMI.mib")
load("mibs/RFC-1212.mib")
load("mibs/rfc1213.mib")
load("./SNMPv2-SMI.my")
load("./SNMPv2-TC.my")
load("./SNMPv2-CONF.my")
load("mibs/rfc2819.mib")

m = M(ip, community="public", version=1)
#print(m.sysUpTime)
#print(m.sysContact)
#m.sysContact = "Georg"
#print(getattr(m, "sysContact"))
#setattr(m, "sysContact", "Admin")
#print(getattr(m, "sysContact"))
if (check):
	checker(m)
else:
	setter(m)
	checker(m)


