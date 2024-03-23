//const employees = [
 // {'name': 'person','adress': 'kampala'}
//]
//const employees =[
 // {name: 'peter', amount:2500000}
 // {name: 'Isaac', amount:1500000}
  //{name: 'Jane', amount:300000}
  //{name: 'John', amount:4000000}
  //{name: 'Betty', amount:700000}
//]

function calculateAverage(numbers){
  let sum = 0;
  console.log(nubers.length)
  for (let i = 0; i <= numbers.length; i++) {
    console.log('At position: ${i} the the number is: ${numbers[i]}');
    sum += numbers[i];
  }
  return sum /numbers.length;
}
const numbers = [10,20,30,40,50];
const avg = calculateAverage(numbers);
console.log('the average is:$(avg)');
