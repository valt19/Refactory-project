#a named block of code is called a function
# a function is a group of statements/code related to one another and performs a specific task
def myfunction():
  num1,num2 = 20,40
  print(num1 + num2)
myfunction()
# there are two types of functions named static and functions
 
#condition
def condition():
  number = 10
  if number > 0:
    print("number is positive")
  print("if statement is easy") # from line 11to line 14 , its a function definition 
#condition() 
#below code has been extracted from the function
number  = 10
if number > 0:
  print("number is positive")   

number = 40
if number > 0:
  print("number is your age ")
print("not really")
#the calling of a function is invoke
condition() 
 
#below code is when we have removed/extracted from the function
number = 10
if number > 0:
  print("number is your age ")
print("not really")

"""
function condition(){
  this is a function written in javascript  
}
"""
def mycondition():
  number = -20
  if number > 0:
    print("number is positive")
  else:
    print("number is negative")
  print("this statement is not related to if or else but in the same function")  
mycondition()  

