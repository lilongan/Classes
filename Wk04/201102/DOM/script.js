
//script.js
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