document.getElementById('theme-toggle').addEventListener('click', () => {
    const body = document.body;
    body.classList.toggle('dark');
    const isDark = body.classList.contains('dark');
    const button = document.getElementById('theme-toggle');
});
