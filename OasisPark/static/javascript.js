const express = require('express');
const session = require('express-session');
const bodyparser = require('body-parser')

const port = 5008;
var path = require('path');
const app = express();

app.use(session({secret:'ksdmnalksdnmalksdnmaksd'}));

app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.use('/public', express.static(path.join(__dirname, 'public')));
app.set('views', path.join(__dirname, '/views'));

app.post('/login',(req,res)=>{

})

app.get('/login',(req,res)=>{
    res.render('login.html');


})

app.listen(port, ()=>{
    console.log()
})



























(function(win, doc){
    'use strict';
    //Verifica se o usuário deseja mesmo deletar este dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event ){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

})(window, document);

