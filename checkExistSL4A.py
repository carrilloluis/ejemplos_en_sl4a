#-*-coding:utf8;-*-
#qpy:console

__author__ = u'Luis Carrillo Gutiérrez'

try:
    import androidhelper as sl4a
except ImportError:
	import android as sl4a
except ImportError:
    import sl4a

print('\033[2J') # clear screen
app = sl4a.Android()
print('Se ha cargado SL4A, con éxito!')