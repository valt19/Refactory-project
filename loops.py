#a loop is a mechanism in programming or means of writing instructions to a computer to repeatedly do an action .
mylist =[10, 20, 30,40,50]
mylist2 =[0,1,2,3,4,5,6,7,8,9,10]
# an iteration/repeatation  of values in a list of numbers 

#for loop
for i in mylist:
  print(i)
for i in range (10):
  print(i)

item = 1
for item in range(1,10): #1 represents the start and 10 represents the end of the list. 
  print(item)
  #range is a keyword in python.
  #loops are very costly in terms of memory comsumption.
  #two types of loops that is "for' loop and "while" loop.

  for i in range (1,20):
    if i % 2 == 0:
      print(i)
for i in range(1,20):
  if i % 2 != 0:
    print(i)
    # a block of code is a collection of related statements
    # a block of code is identified by indentation.

mydigits =[23,67,50,70,89]
for i in mydigits:
  print(i)
else:
    print("no items left")


    #while loop
begin = 1
end = 5
while begin <= end:
  print(begin)
  begin += 2

counter = 0
while counter < 5:
  print("these are the numbers in the range given")
  counter += 1
else:
  print("out of range")  
  # case switch break and continue 
   