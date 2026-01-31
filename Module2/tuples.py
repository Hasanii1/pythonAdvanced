fruits = ["apple", "bannana", "cherry"]
#print(fruits)
#fruits[1]= "orange"
#print(fruits)


#Tuples
words = ("spam", "eggs", "ham")
#words[1] = "sausage" - kemi error sepse nuk mund te ndryshohet nje tuple element
print(words[-2])#printon elementin e dyte nga fundi
print(len(words)) #printon gjatesine e tuple

person = ("Gresa", 23, "Engineer")

name, age, profession = person
print(name,"'s age is", age, "and profession is", profession)