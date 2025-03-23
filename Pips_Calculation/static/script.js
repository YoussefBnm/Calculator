// JavaScript for animations and interactivity

// Function to animate button clicks
document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('button');
    
    button.addEventListener('click', function() {
        button.classList.add('clicked');
        setTimeout(() => {
            button.classList.remove('clicked');
        }, 300);
    });
});
