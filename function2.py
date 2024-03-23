def add():
  num1,num2 = 10,20 
  sum = num1 + num2
  print(sum)
add()  
#creating a dynamic function
def add1(num1,num2):
  sum = num1 + num2
  print(sum)
   
add1(100,50)
add1(200,45)
add1(45,75)
def sub1(num1,num2):
  sub = num1 - num2
  print(sub)
   
sub1(100,50)
sub1(200,45)
sub1(45,75)
def div1(num1,num2):
  div = num1 / num2
  print(div)
   
div1(100,50)
div1(200,45)
div1(45,75)
def mult1(num1,num2):
  mult = num1 * num2
  print(mult)
   
mult1(100,50)
mult1(200,45)
mult1(45,75)
def expo1(num1,num2):
  expo = num1 ** num2
  print(expo)
   
expo1(100,50)
expo1(200,45)
expo1(45,75)
def mod1(num1,num2):
  mod = num1 % num2
  print(mod)
   
mod1(100,50)
mod1(200,45)
mod1(45,75)
def floordiv1(num1,num2):
  floordiv = num1 // num2
  print(floordiv)
   
floordiv1(100,50)
floordiv1(200,45)
floordiv1(45,75)

def multidata1(num1,num2,name,flt):
  print(num1)
  print(num2)
  print(name)
  print(flt)
multidata1(10,50,"val",20.2)

def data1(district,num2,name,flt,int):
  print(district)
  print(num2)
  print(name)
  print(flt)
  print(int)
data1("Tororo",50,"val",20.2,89)

def data1(country,district,num,name,flt,color):
  print(country)
  print(district)
  print(num)
  print(name)
  print(flt)
  print(color)
data1("Uganda","Tororo",50,"val",20.2,"blue")

def multidata2(name,yob,district):
  #print(name)
  #print(yob)
  #print(district)
  currentyear  =2024
  age =currentyear - yob
  print(name,"is",age)
multidata2("val",2002,"Tororo") 

def data2(country,district,yob,name,color):
  print(country)
  print(district)
  print(yob)
  print(name)
  print(color)
  currentyear = 2024
  age = currentyear -yob
  print(name,"is",age)
data2("Uganda","Kaberamaido",2001,"val","blue")

def data3(country,district,yob,name,city_code,years_active):
  print(country)
  print(district)
  print(yob)
  print(name)
  print(city_code)
  print(years_active)
  currentyear = 2024
  age = currentyear -yob
  print(name,"is",age)
data3("Uganda","Kaberamaido",2001,"val",0000,15)



function divide(a, b) {

    return a / b;

}



function main() {

    const rl = readline.createInterface({

        input: process.stdin,

        output: process.stdout

    });



    rl.question("Enter a number: ", function(x) {

        rl.question("Enter another number: ", function(y) {

            try {

                let num1 = parseInt(x);

                let num2 = parseInt(y);

                

                if (isNaN(num1) || isNaN(num2)) {

                    throw new Error("Invalid input. Please enter valid numbers.");

                }

                

                let result = divide(num1, num2);

                console.log("Result of division:", result);

            } catch (error) {

                console.error("An error occurred:", error.message);

            } finally {

                rl.close();

            }

        });

    });

}



main();