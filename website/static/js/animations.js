// Importing required styles
import { animationStyle } from '../css/animations.css';

// Function to apply animations
function applyAnimation(elementId, animationName) {
    let element = document.getElementById(elementId);
    if (element) {
        element.style.animation = animationStyle[animationName];
    }
}

// Applying animations to navbar
applyAnimation('navbar', 'slideIn');

// Applying animations to footer
applyAnimation('footer', 'fadeIn');

// Applying animations to contact form
applyAnimation('contactForm', 'bounceIn');

// Applying animations to services list
applyAnimation('servicesList', 'zoomIn');