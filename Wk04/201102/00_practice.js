// 1. Write a program that will declare a variable named "value".
//     Have an if, if else, else statement that compares that value.


let a = 22
//if statement
if(a == 22){
    console.log('a is 22')//not print
}
//if else statement
if(a == 12){
    console.log('a is 12')
} else {
    console.log('a is not 12')
}

//if else if else
if(a < 22){
    console('a is less than 22')
} else if (a < 23) {
    console.log('a is less than 23')
} else {
    console.log('a is larger than 23')
}

// VM250:4 a is 22
// VM250:10 a is not 12
// VM250:17 a is less than 23
// undefined

// 2. Using ternary.

//     compare if one number is greater than another.
//     set the value of a variable named 'result' to 'higher' if the first number is higher and lower if the first number is lower.

let a = 22, b = 33
if (a == 22) {
    let result = 'a is 22';
    if (a !== 33) {
        let result = 'a is not 33';
} else if (a > 33) {
    let result = 'higher';
} else {
    let result = 'lower';
}
console.log ('result')

// 3. Using switch.
// set a variable named = 'temp' and give it a value between -20 & 110.
// Have cases for sub 0, 30, 50, 75, 80, 90, and above.
// Have a hex color for each level going from blue to red.
// print out the color that represents the range.

let temp = 30
let color = null

switch (true) {
    case (temp < 0):
        color = '#0000cc';
        break;
    case (temp < 30):
        color = '#0066ff';
        break;
    case (temp < 50):
        color = '#66ccff';
        break;
    case (temp < 75):
        color = '#ccffff';
        break;
    case (temp < 80):
        color = '#ffccff';
        break;
    case (temp < 90):
        color = '#ff6699';
        break;
    default:
        color = '#ff0000';
}
console.log(color);

// Crystal Atkinson answer:
let temp = 73
let color = null
switch (true) {
    case (temp < 0):
       color = '#0000cc'
       break;
    case (temp< 30):
        color = '#0066ff'
        break;
    case (temp< 50):
        color = '#66ccff'
        break;
    case (temp< 75):
        color = '#ccffff'
        break;
    case (temp< 80):
        color = '#ffccff'
        break;
    case (temp< 90):
        color = '#ff6699'
        break;
    default:
        color = '#ff0000'
} 
console.log(color)

// 1. Using a while loop add numbers from 1 to 10.

let x = 0;
while (x < 11) {
  console.log(x);
  x++;
}

// 2. Using a for loop, count from a number of your choice to another number.
for(let i = 5;i<10;i++){
    if(!(i % 2)) continue;
    console.log(i)
}

