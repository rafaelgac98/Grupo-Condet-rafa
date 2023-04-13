


/*function shUser() { // Exibe os valores de "username" e "expires" no cookie
  let c = "username: " + getUser() + " - expires: " + getExpires();
  document.getElementById( "saida" ).innerHTML = c;
}*/

function setUser(user) { // Cria o cookie com as chaves "username" e expires
    let userid = "username=" + user;
  
    let d = new Date();
    d.setTime( d.getTime() + 10 * 60 * 1000 ); // Este cookie expira em 10 minutos (10*60*1000 miliseg.)
    let expires = "expires="+ d.toUTCString();
  
    let c  = userid;
    document.cookie = c;
    //window.location.href = "menu-principal.html";
  }
  
  function getUser() { // Procura o valor da chave "username" no cookie
    let decodedCookie = decodeURIComponent(document.cookie); // Limpa caracteres especiais no cookie
    let ca = decodedCookie.split( ';' ); // Quebra o cookie numa lista de strings nos ";"
    for( let i = 0; i < ca.length; i++ )
      if( ca[i].indexOf( "username=" ) == 0 ) // Se tem a chave "username="
        //window.location.href = "menu-principal.html";
        return ca[i].substring( "username=".length, ca[i].length ) // retorna seu valor
  
      return ""; // Não tem "username=" no cookie
  }
  
  function getExpires() { // Procura o valor da chave "expires" no cookie
    let decodedCookie = decodeURIComponent(document.cookie); // Limpa caracteres especiais no cookie
    let ca = decodedCookie.split( ';' ); // Quebra o cookie numa lista de strings nos ";"
    for( let i = 0; i < ca.length; i++ )
      if( ca[i].indexOf( "expires=" ) == 0 ) // Se tem a chave "expires="
        return ca[i].substring( "expires=".length, ca[i].length ); // retorna seu valor
  
    return ""; // Não tem "expires=" no cookie
  }
  
  function GetforUser(){
    let decodedCookie = decodeURIComponent(document.cookie); // Limpa caracteres especiais no cookie
    let ca = decodedCookie.split( ';' ); // Quebra o cookie numa lista de strings nos ";"
    for( let i = 0; i < ca.length; i++ )
      if( ca[i].indexOf( "username=" ) == 0 ) // Se tem a chave "username="
        return ca[i].substring( "username=".length, ca[i].length ) // retorna seu valor
  
      return "";
  
  }
  
  function Logout(){
    var c = document.cookie.split("; ");
    for (i in c) 
     document.cookie =/^[^=]+/.exec(c[i])[0]+"=;expires=Thu, 01 Jan 1970 00:00:00 GMT"
  
    window.location.href = "login.html";
  }
  
  
  function register() {
    const xhttp = new XMLHttpRequest();
  
    xhttp.onreadystatechange = function() {
        console.log("readyState:" + this.readyState);
        console.log("status:" + this.status);
  
        if (this.readyState == 4 && this.status == 200) {
        imprimeResposta(this);
        
        }
    };
  
    xhttp.onload = function() {
        //document.getElementById("resposta").innerHTML = this.responseText;
        alert(this.responseText);
    };
  
    
    var data = {
    "from": document.getElementById("userRegister").value,
    "email":document.getElementById("email").value,
    "password":document.getElementById("passwordRegister").value};
    var jsondata = JSON.stringify(data);
    var url = "http://127.0.0.1:5008/login";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(jsondata);
  }
  
  function imprimeResposta(xml) {
  var xmlDoc = xml.responseXML;
  document.getElementById("resposta").innerHTML = xmlDoc;
  }
  
  function getUser(){
    //document.getElementById("saida").innerHTML = "Mensagem recebida";
    var xhttp = new XMLHttpRequest();
    var user = document.getElementById("userLogin").value;
    var url = "http://127.0.0.1:5008/login?userLogin=" + user;
    var pass = document.getElementById("passwordLogin").value;
  
    //xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.onload = function () {
  
            if (xhttp.readyState == 4 && xhttp.status == "200") {
                  
              if( pass == this.response){
                setUser(user);
                alert("Login com sucesso!")
                window.location.href = "/";
              }else{
                alert("Usuário ou senha incorretos. Por favor, tente novamente!")
              }
            }
        }
    xhttp.open("GET", url, true); //GET: a consulta vai no cabeçalho com a URL
    xhttp.send();
  
  }