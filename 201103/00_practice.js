// /1. Write a function that accepts 3 arguments and returns the value of all 
// the items added together.

function sum(x, y, z) {
    return x + y - z;
    // code after the return will not run
  }
  var sumOfNumbers = sum(5, 7, 2);
  console.log(sumOfNumbers); // 12
  


// 2. Write a function that has an anonymous function as the first argument and 
// a number as the second argument.

//     . the anonymous function needs to console.log something.
//     . Have the first function count from 0 to the number that 
//       the second argument is.
//     . After it is done counting have it call the anonymous function.
//     . call the function again with a different function as the argument.

// Exercises JavaScript 101 8-Objects
//     1. Create an object called 'spaceship'.
//         give it the following keys with whatever values seems reasonable to you. 
//         speed,acceleration, passangers, fuel.
//     2. Using the spaceship object above add a payload key after the object 
//         has been created. (just give it a number)
//     3. Using the same object above, lower the amount of fuel by 1/3.
//     4. loop through the object and give a message to the console like 
//         the one below for every property in the object.

let spaceship = [{
    speed:0,
    acceleration:60,
    passangers:'Ian' 'Art' 'Lynn',
    fuel:90
}]
let myObj = {
    payload:22
}
for(attrib in spaceship){
    if(!spaceship.fule/3(attrib)) continue;
    console.log(attrib)
    console.log(spaceship[attrib])
}

// Exercises JavaScript 101 9-arrays of objects
//   1. Make an array of ship objects (at least 3). Each ship needs a 
//           name, topSpeed, acceleration, and cargo capacity.
//         console.log the name and top speed of the 2nd ship.
//         loop through the array and print out every stat in a key:value style.
//         (Bonus) sort the array by the ship with the fastest speed and 
//           console log it out.

let ship = [
    {
        name:"Olympic",
        topSpeed:38,
        acceleration:15,
        cargoCapacity:150
    },
    {
        name:"Titanic",
        topSpeed:37,
        acceleration:10,
        cargoCapacity:150
    },
    {
        name:"Britanic",
        topSpeed:11,
        acceleration:5,
        cargoCapacity:150
    }
]
consule.log(ship[1].name,ship[1].topSpeed('-'))

//single item
// ships.forEach(function(ship){
//     console.log(ship)
ships.forEach(function(ship)
    console.log('**********')
    for(key in ship){
        console.log(' ${key} : ${ship[key]} ')
    }
    console.log('**********')
})
ships.sort(function(a,b){
    return a.topSpeed - b.topSpeed    
})
.reverse()
console.log(ship)





