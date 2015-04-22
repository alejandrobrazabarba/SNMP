#!/usr/bin/python
import sys
from snimpy.manager import Manager as M
from snimpy.manager import load
import time

#Orden de carga correcto
load("mibs/RFC1155-SMI.mib")
load("mibs/RFC-1212.mib")
load("mibs/rfc1213.mib")
load("./SNMPv2-SMI.my")
load("./SNMPv2-TC.my")
load("./SNMPv2-CONF.my")
load("mibs/rfc2819.mib")#MIB de RMON
#########################
ip="192.168.0.197:8001"
m = M(ip, community="public", version=2)
topspeed=10 #MegaBits por segundo
def calculaUtilizacion(oldcounter,newcounter,interval,topspeed):
	#Ancho de banda empleado en bytes por segundo
	usedspeed=(newcounter-oldcounter)/interval
	#
	utilizacion= (usedspeed*8)/(topspeed*1e6);
	return utilizacion

#def barraLed(utilizacion)
	
#oldcounter=0

#while True:
	#tiempo=m.sysUpTime
	#print(tiempo)
#	paquetes=m.ifInOctets[3]
	#print(paquetes)
#	utilizacion=calculaUtilizacion(oldcounter,paquetes,2,topspeed)
#	oldcounter=paquetes
#	print(utilizacion)
#	time.sleep(2)

m.etherStatsStatus[4]=2
m.etherStatsStatus[5]=3
m.etherStatsStatus[6]=2

	
