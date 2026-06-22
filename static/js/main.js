/**
 * Godrej Toothpaste Smart Marketplace
 * Main JavaScript - Navigation, animations, and UX enhancements
 */

document.addEventListener('DOMContentLoaded', function () {
    initThemeToggle();
    initMobileMenu();
    initFlashAutoDismiss();
    initScrollAnimations();
    initNavbarScroll();
});

/**
 * Light / dark mode toggle with localStorage persistence
 */
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    toggle.addEventListener('click', function () {
        const html = document.documentElement;
        const nextTheme = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', nextTheme);
        localStorage.setItem('theme', nextTheme);
        toggle.setAttribute(
            'aria-label',
            nextTheme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
        );
    });

    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    toggle.setAttribute(
        'aria-label',
        currentTheme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
    );
}

/**
 * Mobile hamburger menu toggle
 */
function initMobileMenu() {
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    if (!hamburger || !navLinks) return;

    hamburger.addEventListener('click', function () {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        hamburger.setAttribute(
            'aria-expanded',
            navLinks.classList.contains('active')
        );
    });

    // Close menu when a link is clicked
    navLinks.querySelectorAll('.nav-link').forEach(function (link) {
        link.addEventListener('click', function () {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function (e) {
        if (!hamburger.contains(e.target) && !navLinks.contains(e.target)) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });
}

/**
 * Auto-dismiss flash messages after 5 seconds
 */
function initFlashAutoDismiss() {
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(function (flash) {
        setTimeout(function () {
            flash.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            flash.style.opacity = '0';
            flash.style.transform = 'translateX(100%)';
            setTimeout(function () {
                flash.remove();
            }, 400);
        }, 5000);
    });
}

/**
 * Intersection Observer for scroll-triggered animations
 */
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll(
        '.product-card, .review-card, .about-row, .contact-card'
    );

    if (!('IntersectionObserver' in window)) return;

    const observer = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );

    animatedElements.forEach(function (el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

/**
 * Add subtle shadow to navbar on scroll
 */
function initNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    window.addEventListener('scroll', function () {
        if (window.scrollY > 10) {
            navbar.style.boxShadow = '0 4px 20px rgba(0, 84, 97, 0.15)';
        } else {
            navbar.style.boxShadow = '0 4px 20px rgba(0, 84, 97, 0.1)';
        }
    });
}
