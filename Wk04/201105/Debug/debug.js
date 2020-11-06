//1
let footer = document.querySelector(".footer");//should find the footer elements

//2
let i = document.querySelector('.child-idea') 
for(let i = 0; i < i.length; i++){
    console.log(i) // should console log each idea
}

//3
let ps = document.getElementsByTagName("p")

ps.forEach(function(p){
    console.log(ps) // shows each p's attributes as an object
})
