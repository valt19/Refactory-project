# variable syntax for python(#represents a comment)
# variable names should not start with special characters , eg(#number ,@,$,*)
# variable names should not start with numerical number, eg (1number,2number)
# however ,number1,number2 is a valid syntax
# variable names should not have spaces, eg (my age,my name)
# composite variable names should be seperated by an underscore, eg (my_age,my_name) or you can use camel-case notation,eg (myAge,myName)
#names should not start with capital letters unless they are functions or classes,eg (Myname)
#we should use relatable names, eg (when dealing with a customer , call them mycustomer, when dealing with numbers use num1,num2)
#use shorter names,eg (cust for customer ,age instead of myage)
# variable names should not be repeated in different forms because python is case sensitive,eg ('Name'and 'name' are not the same)
age = 26
name = "Val"
school = "refractory"
print(school)
#declaring variables is a process of naming computer memory spaces
# innitializing variables is the process of giving variables a value,eg (age is a variable,26 is its value)
cntry = "uganda"
# the '=' sign is called the assignment 
# datatypes in python (numeric,string,sequence,mapping,boolean,set,)
#numeric(int,float,complex)
num1 = 19
print(num1, "is of a type", type(num1))
num2 = 0.7
print(num2, "is of a type", type(num2))
num3 = 1+2j
print(num3, "is of a type",type(num3))
#strings (a string is a group of characters eg name="val" or name='val')
name="val"
print(name,"is of a type",type(name))
#semantics is the meanin of what you've written
#typecasting
numx="20"
print(numx,"is of a type",type(numx))
#example of typecasting
numy=float(numx)# conversion of the value of numx into an integer and store it in numy
print(numy,"is of a type",type(numy))
numy=str(numx)
print(numy,"is of a type",type(numy))
numy=int(numx)
print(numy,"is of a type",type(numy))
#sequence data type(under sequence we have lists,turples,and range)
#list is a variable that can store more than one value , however we can have an empty list and we can store values later on
mylist=[]
mylist.append("val")
print(mylist)
mylist.append(3653)
print(mylist)
#append is a specialized comand in python used to add values to a list
#print is a specialized command in python used to output values on a computer screen
#pop is udes to remove the last value of the list
language=["python","javascript","c","c++","c#","swift","julia","ruby","cobol"]
print(language[5])
print(language[0])
print(language[4],language[2])
print(language[-1])
cntry=["uganda","kenya","tanzania",["egypt","somalia",["sudan",["burundi",["togo"],["benin"]]]]]
print(cntry[3][2])
print(cntry[-1][-1])
print(cntry[3][2][0])
print(cntry[-1][-1][-1])
print(cntry[-1][-1][-1][-1])
print(cntry[-1][-1][-1][-2])
print(cntry[-1][-1][-1][-2][-1])
print(cntry[3])
fruits=["apples","mangoes","oranges",['pawpaws',"pears"]]
print(fruits[0])
print(fruits[2])
print(fruits[-2])
print(fruits[-1])
print(fruits[-1][-1])
print(fruits[-1][-2])
# a list is a mutable datatype because it can be manipulated after it has been created
#tuples are imutable datatypes meaning once you create them with elements they can't be changed
#tuples can be type casted thus you can change a list into a tuple but you cant change a tuple to a list 

#mapping
person={"name": "Val", "age":3,"cntry":"Sweden","height":200}
print(person["height"])
print(person.keys())
print(person.values())

#set
student_id ={200,300,400,500,600,600}
print(student_id)
print(student_id)
