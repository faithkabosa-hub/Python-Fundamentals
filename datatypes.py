from variables import firstname

age = 19  #Integer
temperature = 34.89  #Float
greeting = "Hello"  #String
isMarried = True  #Boolean

print("I am",age, "years old")
print("The body temperature of the patient is",temperature,"degrees celcius")
print(greeting,"Nancy")
print("Are you married? :",isMarried)


# Data Structures - Multiple values stored in a single variable
cars = ["Toyota","Mercedes","Audi","BMW"] #List - Order and changeable
languages = ["Python","Java","C++"] #Array - Similar datatypes

fruits = ("Banana","Apple","Mango","Grape","Pineapple" ) #Tuple - Ordered and unchangeable
countries = {"Italy","Germany","France","Sweden"} #Set - Unordered and unchangeable
student = {
    "firstname" : "John Smith",
    "age" : 19,
    "course" : "Fullstack",
    "gender" : "Male",
} #Dictionary

print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])

# Typecasting - Converting from one datatype to another
print(int(temperature))
