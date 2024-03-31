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


function startLoader() {
    let counterElement = document.querySelector(".counter");
    let currentValue = 0;

    function updateCounter() {
        if(currentValue === 100){
            location.href="home1.html";
            return;
        }

        currentValue += Math.floor(Math.random() * 10) + 1;

        if(currentValue > 100){
            currentValue = 100;
        }

        counterElement.textContent = currentValue;

        let delay = Math.floor(Math.random()*200) + 50;
        setTimeout(updateCounter, delay);
    }

    updateCounter();


}

startLoader();

gsap.to(".counter", 0.25,{
    delay: 0.5,
    opacity: 0,
});

gsap.to(".bar", 1.5, {
    delay: 0.5,
    height: 0,
    stagger: {
        amount: 0.5
    },
    ease: "power4.inOut",
});

gsap.from(".h1", 1.5, {
    delay: 0.5,
    y: 700,
    stagger: {
        amount: 0.5,
    },
    ease: "power4.inOut",
});

gsap.from("nav", 1.5, {
    delay: 0.9,
    y: 700,
    stagger: {
        amount: 0.5,
    },
    ease: "power4.inOut",
});

gsap.from(".corpo", 1.5, {
    delay: 0.8,
    y: 700,
    stagger: {
        amount: 0.5,
    },
    ease: "power4.inOut",
});

