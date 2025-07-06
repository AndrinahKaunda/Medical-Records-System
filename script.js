//login page -wrapper
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const loginPopup = document.querySelector('.login-popup');
const closeIcon = document.querySelector('.close');

registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
});
loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
});
loginPopup.addEventListener('click', ()=>{
    wrapper.classList.add('active-popup');
});
closeIcon.addEventListener('click', ()=>{
    wrapper.classList.remove('active-popup');
});