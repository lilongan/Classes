// script.js

alert('Look I am loaded')
console.log('This is in the console.')

let paragraphs = document.getElementsByTagName("p")
console.log(paragraphs)
console.dir(paragraphs)

// let paragraphs = document.getElementsByClassName("child-idea")
// console.log(paragraphs) // [are these two lines LrnPrtl typos?]

let child = document.getElementsByClassName("child-idea")
console.log(child)
console.dir(child)

let main = document.getElementById("main-idea")
console.log(main)
console.dir(main)

let password = document.querySelector('#password')
console.log(password)
console.dir(password)

let link = document.querySelectorAll('.link')
console.log(link)
console.dir(link)

const heading = document.querySelector('#heading')
heading.innerText = 'Links h2' // Chg html text from js
heading.style.color = "rgb(255, 0,0)" // Chg font color from black to red
console.log(heading)
console.dir(heading)

const headingText = heading.innerText
console.log(headingText)
console.dir(headingText)

const listItems = document.getElementsByTagName('li')
console.log(listItems)
console.dir(listItems)

const listItemsByClass = document.querySelectorAll('.nav-link')
console.log(listItemsByClass)
console.dir(listItemsByClass)

const listItemsLength = listItemsByClass.length
console.log(listItemsLength)
console.dir(listItemsLength)

let regularExpressionConstructor = new RegExp("abc");
let regularExpressionLiteral = /cba/;

const myRegex = /Hello World/
const test = myRegex.test("Hello World")
console.log(test)
console.log(myRegex)

// const button = document.querySelector('#myButton')
//   button.addEventListener('click', function() {
//   alert('click')
// })  // Allows for multiple event clicks on top h1 only

// const button = document.querySelector('#myButton')
// button.addEventListener('click', function() {
//   alert('click')
// })  // Allows for multiple event clicks on top h1 only

const button = document.querySelector('#myButton')
function clickOnce(){
  alert('click')
  button.removeEventListener('click', clickOnce)
}  // Allows for single event click on top h1 only
  button.addEventListener('click', clickOnce)
  console.log(button)
  console.dir(button)
  console.log(myButton)
  console.dir(myButton)

  window.addEventListener('resize', function(){
    console.log(window.innerWidth)
  })

  document.addEventListener('click', event => {
    if(event.target.classList.contains('box')){
      event.target.style.backgroundColor = 'green'
      event.target.innerText = 'Changed'
    }

  })

const headerElement = document.createElement('h1')
headerElement.innerText = "js added h1"
const listElement = document.createElement('ol')
const listItemOne = document.createElement('li')
listItemOne.innerText = "js added listItemOne ol li"
const listItemTwo = document.createElement('li')
listItemTwo.innerText = "js added listItemTwo ol li"
const listItemThree = document.createElement('li')
listItemThree.innerText = "js added listItemThree ol li"
const root = document.querySelector('#root')
root.append(headerElement)
root.append(listElement)
listElement.append(listItemOne, listItemTwo, listItemThree)

headerElement.id = "heading"
listElement.id = "nav-list"

listElement.childNodes.forEach(item => {
  item.className = "nav-link"
})

const form = document.querySelector("form");
const nameInput = document.querySelector("#name");

function checkName() {
  const myRegex = /[A-Za-z]+/;
    if (!myRegex.test(nameInput.value)) {
      nameInput.setCustomValidity(
        "Please use only lowercase or uppercase letters, no numbers"
      );
    } else {
      nameInput.setCustomValidity("");
    } // See, MDN - Constraint Validation API 
} // See also, DcLp CSS: invalid
nameInput.addEventListener("change", checkName, false);

console.log(form)
