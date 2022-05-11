#Python Classes
#Class is an object constructor
#Every object belongs to a class


fruits = ["Banana", "Oranges", "Apples"]
numbers = 1, 2, 3

print(type(fruits))
print(type(numbers))


print(type(numbers))



def function(hello):
	print("Hello")
print(type(function))



#Classes
#Class is an object constructor

class ClassName():  #Note the uppercase letters in the class
	a = 10   #we have created an object'a' inside a class

a1 = ClassName()
print(a1.a)	
print(a1)

class Cat:
	def meow(self):    #function inside a class aka method....so #method is basically a function inside a class
		print("meows")   #all of this is an object in a class
		

c_cat = Cat()	 #creating an instance for the class
c_cat.meow()
print(c_cat)	


#__init__() Function
#helps to assing values to object properties

class Population:
	def __init__(self, names, age):
		self.names = names
		self.age = age

person1 = Population("John", 20)		
person2 = Population("Mary", 25)

print(person1.names) 
print(person1.age)

print(person2.names) 
print(person2.age)


class PeopleData:
	c = 15
p1 = PeopleData()  #creating an instance for the class

print(type(p1))	



class Popu:

	def __init__(self, namez, ages):
		self.namez = namez
		self.ages = ages

	def get_name(self):
		return self.namez

	def get_ages(self):
		return self.ages	

nm = Popu("Joy", 25)

print(nm.get_name())
print(nm.get_ages())

pront("hello world")

















