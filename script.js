let email = document.getElementById("email");
let password = document.getElementById("senha");
let entrar = document.getElementById("btn");
let Criar = document.getElementById("btn2");
var mensagemErro = document.getElementById("mensagemErro");

entrar.addEventListener("click", function(event) {
  event.preventDefault();
  var senhaDigitada = document.getElementById("senha").value;
  if (senhaDigitada === "01") {
    alert("Login bem-sucedido!");
  } else {
    mensagemErro.style.display = "block";
    setTimeout(function() {
      mensagemErro.style.display = "none";
    }, 1500); 
  }
});

Criar.addEventListener("click",function(){
    window.location.href = "https://www.facebook.com/campaign/landing.php?";
})

