let toggleBtn = document.getElementById('toggle-btn');// Seleciona o botão de alternância (dark mode) pelo ID 'toggle-btn'
let body = document.body;// Seleciona o elemento <body>
let darkMode = localStorage.getItem('dark-mode');// Obtém o estado do modo escuro armazenado no localStorage

// Função para habilitar o modo escuro
const enableDarkMode = () =>{
   toggleBtn.classList.replace('fa-sun', 'fa-moon');// Substitui o ícone de 'fa-sun' por 'fa-moon' no botão
   body.classList.add('dark');// Adiciona a classe 'dark' ao body, aplicando estilos de modo escuro
   localStorage.setItem('dark-mode', 'enabled');// Armazena no localStorage que o modo escuro está habilitado
}

// Função para desabilitar o modo escuro
const disableDarkMode = () =>{
   toggleBtn.classList.replace('fa-moon', 'fa-sun');// Substitui o ícone de 'fa-moon' por 'fa-sun' no botão
   body.classList.remove('dark');// Remove a classe 'dark' do body, desativando o modo escuro
   localStorage.setItem('dark-mode', 'disabled');// Armazena no localStorage que o modo escuro está desabilitado
}

// Verifica se o modo escuro está habilitado no localStorage e, se sim, habilita o modo escuro
if(darkMode === 'enabled'){
   enableDarkMode();
}

// Adiciona um evento de clique no botão de alternância de tema
toggleBtn.onclick = (e) =>{
   darkMode = localStorage.getItem('dark-mode');// Obtém o estado atual do modo escuro
   if(darkMode === 'disabled'){
      enableDarkMode();
   }else{
      disableDarkMode();// Se o modo escuro estiver desabilitado, habilita-o, senão desabilita
   }
}

let perfil = document.querySelector('.header .flex .perfil');

document.querySelector('#user-btn').onclick = () =>{
   perfil.classList.toggle('active');
   search.classList.remove('active');
}

let sideBar = document.querySelector('.side-bar');

document.querySelector('#menu-btn').onclick = () =>{
   sideBar.classList.toggle('active');
   body.classList.toggle('active');
}

document.querySelector('#close-btn').onclick = () =>{
   sideBar.classList.remove('active');
   body.classList.remove('active');
}

window.onscroll = () =>{
   perfil.classList.remove('active');

   if(window.innerWidth < 1200){
      sideBar.classList.remove('active');
      body.classList.remove('active');
   }
}

/*--------------------------------------------------------------------------*/