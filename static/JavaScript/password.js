let eye_icon = document.getElementsByClassName('im')
    for (let i = 0; i < eye_icon.length; i++) {
        eye_icon[i].addEventListener('click', function () {

            if (this.classList.contains('im-eye-off')) {
                this.classList.remove('im-eye-off')
                this.parentElement.querySelector('input').type = 'text'
                this.classList.add('im-eye')
            } else {
                this.parentElement.querySelector('input').type = 'password'
                this.classList.remove('im-eye')
                this.classList.add('im-eye-off')
            }
        })
    }