// JavaScript code for the dashboard

const button = document.getElementById('dashboard-button');
const content = document.getElementById('dashboard-content');

button.addEventListener('click', () => {
  content.innerHTML = 'Button clicked!';
});