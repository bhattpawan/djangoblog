if (document.querySelector('.alert')) {
    document.querySelectorAll('.alert').forEach(function ($el) {
        setTimeout(() => {
            $el.classList.add('d-none');
        }, 3000);
    });
}