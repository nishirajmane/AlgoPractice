// Main JavaScript file for AlgoPractice

document.addEventListener('DOMContentLoaded', function () {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add fade-in animation to cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe all cards and algorithm items
    document.querySelectorAll('.card, .algorithm-card').forEach(el => {
        observer.observe(el);
    });

    // Copy to clipboard functionality
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const textToCopy = this.getAttribute('data-clipboard-text');
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check"></i> Copied!';
                setTimeout(() => {
                    this.innerHTML = originalText;
                }, 2000);
            });
        });
    });

    // Search functionality enhancement
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function () {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                // Trigger search after user stops typing
                const event = new Event('input');
                searchInput.dispatchEvent(event);
            }, 300);
        });
    }

    // Progress tracking
    function updateProgress() {
        const visitedAlgorithms = JSON.parse(localStorage.getItem('visitedAlgorithms') || '[]');
        const totalAlgorithms = 48; // Total number of algorithms
        const progress = (visitedAlgorithms.length / totalAlgorithms) * 100;

        const progressBar = document.querySelector('.progress-bar');
        if (progressBar) {
            progressBar.style.width = progress + '%';
            progressBar.setAttribute('aria-valuenow', progress);
        }
    }

    // Track algorithm visits
    if (window.location.pathname.includes('/algorithm/')) {
        const algorithmPath = window.location.pathname;
        const visitedAlgorithms = JSON.parse(localStorage.getItem('visitedAlgorithms') || '[]');
        if (!visitedAlgorithms.includes(algorithmPath)) {
            visitedAlgorithms.push(algorithmPath);
            localStorage.setItem('visitedAlgorithms', JSON.stringify(visitedAlgorithms));
        }
    }

    // Initialize progress on page load
    updateProgress();

    // Theme toggle (if implemented)
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            document.body.classList.toggle('dark-theme');
            const isDark = document.body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }

    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
}); 