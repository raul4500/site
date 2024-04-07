var usuario = localStorage.getItem('usuario');
var senha = localStorage.getItem('senha');

if(usuario != "" && senha != "" && usuario != null && senha != null){
document.getElementById('bloco1').textContent = ("usuario: "+usuario+" e "+"senha: "+senha);
document.getElementById('botaologin').style.display = 'none';

}else{
    document.getElementById('iconperfil').style.display = 'none';
    document.getElementById('sair').style.display = 'none';
}

document.getElementById('logout').addEventListener('click', function(){
    localStorage.setItem('usuario', "");
    localStorage.setItem('senha', "");
    location.reload()
});

document.getElementById('iconperfil').addEventListener('click', function(){
    if(document.getElementById('profile').style.display == 'none'){
        document.getElementById('profile').style.display = 'block';
    }else{
        document.getElementById('profile').style.display = 'none';
    }
});
