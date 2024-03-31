var usuario = localStorage.getItem('usuario');
var senha = localStorage.getItem('senha');

if(usuario != "" && senha != "" && usuario != null && senha != null){
document.getElementById('bloco1').textContent = ("usuario: "+usuario+" e "+"senha: "+senha);
document.getElementById('botaologin').style.display = 'none';

}else{
    document.getElementById('iconperfil').style.display = 'none';
    document.getElementById('sair').style.display = 'none';
}

document.getElementById('sair').addEventListener('click', function(){
    localStorage.setItem('usuario', "");
    localStorage.setItem('senha', "");
    location.reload()
});
