from paquete1.modelado import *			# Importamos todos los elementos que se encuentan en el paquete modelado

d=Docente("Docente BD","Loja")			# Creamos un objeto Docente y le enviamos los 2 parametros
d2=Docente("Docente Prog","Quito")		# Creamos otro objeto Docente y le enviamos los 2 parametros
listado=[d,d2]							# Almacenamos ambos objetos en una lista
e=Estudiante("Luis",listado)			# Creamos un objeto Estudiante y enviamos una cadena y la lista 
print(e.presentar_datos())				# Presentamos la cadena que nos devuelva la funcion presentar_datos del objeto Estudiante