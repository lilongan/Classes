let myList = [
    {url:"http://www.google.com", id:"google-link", text:"Goto Google yo!"},
    {url:"http://www.google.com", id:"google-link", text:"Goto Google yo!"},
    {url:"http://www.google.com", id:"google-link", text:"Goto Google yo!"}
]
let ul = document.createElement("ul")
main.append(ul)
myList.forEach(function(item){
    let a = document.createElement("a")
    a.href = item.url;
    a.innerText = item.text;
    let l = document.createElement("li")
    l.append(a)
    ul.append(l)
})




