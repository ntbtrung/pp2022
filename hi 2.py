class Students:
	def __init__(self):
		self.__id = ""
		self.__name = ""
		self.__dob = ""
		
	def getId(self):
		return self.__id
		
	def getName(self):
		return self.__name 
		
	def getDob(self):
		return self.__dob
		
	def setId(self, id):
		self.__id = id
		
	def setName(self, name):
		self.__name = name 
		
	def setDob(self, dob):
		self.__dob = dob
		
		
class Courses:
	def __init__(self):
		self.__id = ""
		self.__name = ""
		
	def getId(self):
		return self.__id
		
	def getName(self):
		return self.__name 
		
	def setId(self, id):
		self.__id = id
		
	def setName(self, name):
		self.__name = name 
	