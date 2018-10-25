from paquete1.modelado import *

d=Docente("Docente BD","Loja")
d2=Docente("Docente Prog","Quito")
listado=[d,d2]
e=Estudiante("Luis",listado)
print(e.presentar_datos())