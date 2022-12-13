class Student: 
	name = "Default" 

	# default constructor 
	def __init__(self): 
		self.name = "Anonymous"
	


	# a method for printing data members 
	def print_student(self): 
		print(self.name) 


# creating objects of the class 
obj1 = Student() 

# calling the instance method using the object obj 
obj1.print_student() # what is printed here?




class Student2: 
	name = "Default" 

	# parameterized constructor 
	def __init__(self,name): 
		self.name = name
	

	# a method for printing data members 
	def print_student(self): 
		print(self.name) 


# creating objects of the class 
obj2 = Student2("Alice") 

# calling the instance method using the object obj 
obj2.print_student() # what is printed here?
