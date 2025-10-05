function clearPostForm() {
    const form = document.querySelector('.post-form');

    // გაწმინდე ტექსტარეა
    const caption = form.querySelector('textarea');
    if (caption) caption.value = '';

    // გაწმინდე file input
    const imageInput = form.querySelector('input[type="file"]');
    if (imageInput) imageInput.value = '';
}


function toggleMenu(icon) {
    const menu = icon.nextElementSibling;
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}
