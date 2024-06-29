/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* Menu show */
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu')
    })
}

/* Menu hidden */
if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu')
    })
}

/*=============== LOGIN ===============*/
const login = document.getElementById('login'),
      loginBtn = document.getElementById('login-btn'),
      loginClose = document.getElementById('login-close'),
      signup = document.getElementById('signup'),
      signupLink = document.getElementById('signup-link'),
      loginLink = document.getElementById('login-link'),
      signupClose = document.getElementById('signup-close')

/* Login show */
if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        login.classList.add('show-login')
        signup.classList.remove('show-signup')
    })
}

/* Login hidden */
if (loginClose) {
    loginClose.addEventListener('click', () => {
        login.classList.remove('show-login')
    })
}

/* Show signup form */
if (signupLink) {
    signupLink.addEventListener('click', (e) => {
        e.preventDefault()
        login.classList.remove('show-login')
        signup.classList.add('show-signup')
    })
}

/* Show login form */
if (loginLink) {
    loginLink.addEventListener('click', (e) => {
        e.preventDefault()
        signup.classList.remove('show-signup')
        login.classList.add('show-login')
    })
}

/* Signup hidden */
if (signupClose) {
    signupClose.addEventListener('click', () => {
        signup.classList.remove('show-signup')
    })
}
    // Redirige l'utilisateur vers le formulaire de connexion après une inscription réussie
    if (document.querySelector('.success-message')) {
        setTimeout(function() {
            document.getElementById('login-btn').click();
        }, 3000) // Redirige après 3 secondes (3000 millisecondes)
    }
