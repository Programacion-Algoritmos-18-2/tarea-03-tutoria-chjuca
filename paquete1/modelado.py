class Docente:									# Creamos la Clase Docente

 	def __init__(self,n,a):						# Creamos el Metodo __init__
 		self.nombre=n 							# Atributo nombre de la clase Docente 
 		self.ciudad=a 							# Atributo ciudad de la clase Docente 

 	def setNombre(self,n):						#Funcion da valor n el atributo nombre
 		self.nombre=n

 	def setCiudad(self,a):						#Funcion da valor a el atributo ciudad
 		self.ciudad=a

 	def getNombre(self):						#Esta funcion devuelve el atributo nombre
 		return self.nombre

 	def getCiudad(self):						#Esta funcion devuelve el atributo ciudad
 		return self.ciudad
 		
 	def presentar_datos(self):					# Presentamos los valores de los atributos nombre y ciudad
 		cadena="%s\n\t%s"%(self.getNombre(),self.getCiudad())
	

class Estudiante:								# Creamos la Clase Estudiante
	"""docstring for Estudiante"""
	def __init__(self,n,listaDocentes):			# Creamos el Metodo __init__
		self.nombres=n 							# Atributo nombres de la clase Estudiante 
		self.docentes=listaDocentes				# Atributo listaDocente la clase Estudiante 

	def setNombre(self,n):						#Funcion da valor n el atributo nombre
		self.nombres=n

	def setDocentes(self,listaDocentes):		#Funcion da valor listaDocentes el atributo docentes
		self.docentes=listaDocentes

	def getNombre(self):						#Esta funcion devuelve el atributo nombre
		return self.nombres

	def getDocentes(self):						#Esta funcion devuelve el atributo docentes
		return self.docentes

	def presentar_datos(self):					#Presentamos los valores de los atributos Nombre 
		cadena="\nEstudiante: %s\n"%(self.getNombre())	
		cadena="%s %s"%(cadena,"Lista Docentes: ")
		for i in self.getDocentes():
			cadena="%s\n\t-%s\n\t\t%s\n"%(cadena,i.getNombre(),i.getCiudad())
		return cadena




		