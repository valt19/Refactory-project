#how to make functions communicate
def vat(rate,price):
  frate = ((rate/100)*price)
  return frate

def net_price():
    actvat = vat(18,200)
    print(actvat)`               `
    actprice = 20000 + actvat 
    print (actprice)

net_price()

#18,200 are arguments 
#price and rate are parameters of the function vat 
#return is the last statement to be executed in a function 


#assignment
#using paramentalized functions create three functions that share the same function name but take  diffirent number of arguments:
#two of them should be dynamic 
#last one should be receiving values from the first two.

#from then and now what are your learning take aways with  examples in code
#python is extremly moduler and object oriented 
