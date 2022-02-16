# BatteryManager Facade

Esta sección expone el API (funciones) para la gestión de la batería.

El orden para usar cualquiera de las funciones etiquetadas (o nombradas) como _batteryGet\*_ , empieza con la llamada previa a _batteryStartMonitoring_, que inicializa la escucha de eventos para la "batería". Se recomienda incorporar una espera de un segundo para mejorar la respuesta.

+ batteryStartMonitoring
Inicia el seguimiento (o la inspección) al estado de la batería y permite la escucha de eventos relacionados con la batería.

+ batteryStopMonitoring
Detiene el seguimiento (o la inspección) del estado de la batería.

+ batteryCheckPresent
Reporta la presencia de la batería en el móvil. (funciona con un Android SDK v5 o superior)

+ batteryGetHealth
Informa sobre la condición de la battería :
	1 - desconocida (unknown)
	2 - buena (good)
	3 - con sobrecarga (overheat)
	4 - sin carga (dead)
	5 - sobre voltaje (over voltage)
	6 - fallo no especificado/identificado (unspecified failure)

+ batteryGetLevel
Reporta el nivel de carga de la batería (porcentaje). Requiere un Android SDK v5 o superior.

+ batteryGetPlugType
Reporta el tipo de conector al que la batería esta conectada.
	-1 - desconocido (unknown)
	0 - desconectado (unplugged)
	1 - cargador con fuente poder de corriente alterna (power source is an AC charger)
	2 - cargador conectado a un puerto USB (power source is a USB port)

+ batteryGetStatus
Reporta el estado de carga en la batería
	1 - desconocido (unknown)
	2 - cargando (charging)
	3 - descargando (discharging)
	4 - sin carga (not charging)
	5 - con carga (full)

+ batteryGetTechnology
Reporta sobre la tecnología de la batería. Requiere un Android SDK v5 o superior.

+ batteryGetTemperature
Reporta la temperatura presente en la batería. Requiere un Android SDK v5 o superior.

+ batteryGetVoltage
Reporta el voltaje presente en la batería. Requiere un Android SDK v5 o superior.

+ readBatteryData
Reporta los datos registrados en la batería.

* * *

Autores originales:
+ Alexey Reznichenko <!-- alexey.reznichenko [at] gmail [dot] com  -->
+ Robbie Matthews  <!-- rjmatthews62 [at] gmail [dot] com -->

Traducción libre:
+ Luis Carrillo Gutiérrez
