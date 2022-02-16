#-*-coding:utf8;-*-
#qpy:console

__author__ = u'Luis Carrillo Gutiérrez'

from time import sleep
try:
	import androidhelper as sl4a
except ImportError:
	import android as sl4a
except ImportError:
	import sl4a

status = ['Desconocido', 'Bueno', 'sobre cargado', 'necesita reemplazo', 'con sobre voltaje', 'falla no específicada']

print('\033[2J')
app = sl4a.Android()
app.batteryStartMonitoring();
sleep(1)
if app.batteryCheckPresent().error == None and bool(app.batteryCheckPresent().result):
	print('\tLa batería está CONECTADA, d\'ohh! ')
# Health's Battery	
print('Estado de la batería : ')
print(status[int(app.batteryGetHealth().result)])	

app.batteryStopMonitoring()
sleep(2)