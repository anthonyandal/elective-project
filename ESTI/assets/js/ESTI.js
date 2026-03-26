document.getElementById('userIcon').addEventListener('click', function(e) {
    e.preventDefault();
    const dropdown = document.querySelector('.dropdown');
    if (dropdown.style.display === 'none' || dropdown.style.display === '') {
        dropdown.style.display = 'block';
    } else {
        dropdown.style.display = 'none';
    }
});

document.addEventListener('click', function(e) {
    const dropdown = document.querySelector('.dropdown');
    const userIcon = document.getElementById('userIcon');
    
    if (!dropdown.contains(e.target) && !userIcon.contains(e.target)) {
        dropdown.style.display = 'none';
    }
});
