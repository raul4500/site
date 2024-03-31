function enviarInformacao() {
    
}

document.getElementById('logar').addEventListener('click', function() {
var usuario = document.getElementById("usuario").value;
var senha = document.getElementById("senha").value;
if(usuario != "" && senha != ""){
    localStorage.setItem('usuario', usuario);
    localStorage.setItem('senha', senha);
    location.href = "home.html";
}else{
    alert('algo errado')
}
})


document.getElementById('logar').addEventListener('click', enviarInformacao()) 

document.getElementById('cadastrar').addEventListener('click', function() {
alert('cadastrado com sucesso!')
location.href = "home.html";
})

document.getElementById('cadastre-se').addEventListener('click', function() {
document.getElementById('sla').style.display = 'none';
document.getElementById('fotologin').src = 'violao_login.png';
document.getElementById('sla1').style.display = 'block';
});

document.getElementById('entrar').addEventListener('click', function() {
document.getElementById('sla').style.display = 'block';
document.getElementById('fotologin').src = 'bateria_login.png';
document.getElementById('sla1').style.display = 'none';
});
