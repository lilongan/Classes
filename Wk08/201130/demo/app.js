const http = require("http");
const express = require("express");
const app = express();
const fetch = require('node-fetch');
// const fs = require ("fs");
const server = http.createServer(app);
const port = 5432;

// let people = require("./data/people.json");

let people = fetch('https://randomuser.me/api/')
    .then(r=>r.json())
    .then(data=>data)

app.get("/", (req,res)=>{
    res.send("<h1>You are home</h1>")
})
app.get("/api", (req,res)=>{
    res.send(people)
})
app.get("/api/:gender", (req,res)=>{
    const {gender} = req.params
    const personGender = people.find((person)=> person.gender == gender)
    res.send(personGender)
})

app.get("/api/type/:id", (req,res)=>{
    const {id,type} = req.params;
    if(!db.hasOwnProperty(type)) return res.send(null)
    const foundPost = db[type].find(item=>item.id == id)
    res.send(foundPost)
})

app.get("/api/:type", (req,res)=>{
    const {type} = req.params;
    res.send(db[type])
})

server.listen(port, ()=>console.log(`listening on port ${port}`))


// const sendFavicon = (req,res)=>{
//             fs.readFile("/favicon.ico",(err,data)=>{
//                 if(err) return res.send(err);
//                 res.send(data)
//             } )
//         }

//         const _404Content = `
//         <!DOCTYPE html>
//         <html> 
//             <head> 
//                 <title>An Error you have found</title>
//             </head>
//             <body>
//                 <h1>404</h1>
//                 <blockquote>"An Error you have found" - Yoda
//                 </blockquote>
//             </body>
//         </html>
//         `;
//         const send404  = (req,res)=>{
//             res.status(404);
//             res.send(_404Content)
//         }

//         app.get("/favicon.ico", sendFavicon)
      
//         app.get("/", serveHome)
//         app.get("/home", serveHome)
//         app.get("/about", (req,res)=>res.send(serveContent("About", "Let's give them something to talk about.")))
//         app.get("/contact", (req,res)=>res.send(serveContent("Contact")))
//         app.get("*", send404)

//         const port = 4430

//         server.listen(port, ()=>console.log(`listening on port ${port}`))

