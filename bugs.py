#user = [
 # {'name': 'Peter', 'amount': 2500000},
  #{'name': 'Isaac', 'amount': 150000},
  #{'name': 'Jane', 'amount': 300000},
  #{'name': 'John', 'amount': 4000000},
  #{'name': 'Betty', 'amount': 700000}  
#]
#totalAmount = sum(user['amount'] for user in user) 

#for element in user:
 # print(f"{element['name']} deposited {element['amount']} and your interest is {element['amount'] * 0.1} and your total amount is {element['amount'] * 1.1}")


  #numbers = [1,2,3,4,5]
  #total = 0
  #for num in numbers:
   #total += num
#  print(f"the su of nuber is:{total}")

 # def calculate_sum(numbers):
  #  sum = 0
  #for num in numbers:
   #   sum += num
  #return sum
  #numbers = [1,2,3,4,'5']
  #result = calculate_sum(numbers)
  #print(f"the sum of numbers is:{result}")

def calculate_average(numbers):
    total = 0
    count = 0
for num in numbers:
      total += num
      count += 1
average = total / count
 return average

numbers = [10,20,30,40,50]
average = calculate_average(numbers)
print("the average is:",average)