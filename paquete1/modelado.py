class Docente:
 	"""docstring for Docente"""
 	def __init__(self,n,a):
 		self.nombre=n
 		self.ciudad=a
 	def setNombre(self,n):
 		self.nombre=n
 	def setCiudad(self,a):
 		self.ciudad=a
 	def getNombre(self):
 		return self.nombre
 	def getCiudad(self):
 		return self.ciudad
 		
 	def presentar_datos(self):
 		cadena="%s\n\t%s"%(self.getNombre(),self.getCiudad())
	
class Estudiante:
	"""docstring for Estudiante"""
	def __init__(self,n,listaDocentes):
		self.nombres=n
		self.docentes=listaDocentes
	def setNombre(self,n):
		self.nombres=n
	def setDocentes(self,listaDocentes):
		self.docentes=listaDocentes
	def getNombre(self):
		return self.nombres
	def getDocentes(self):
		return self.docentes

	def presentar_datos(self):
		cadena="\nEstudiante: %s\n"%(self.getNombre())
		cadena="%s %s"%(cadena,"Lista Docentes: ")
		for i in range(0,len(self.docentes)):
			cadena="%s\n\t-%s\n\t\t%s\n"%(cadena,self.docentes[i].getNombre(),self.docentes[i].getCiudad())
		return cadena




		