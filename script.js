//login page -wrapper
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const loginPopup = document.querySelector('.login-popup');
const closeIcon = document.querySelector('.close');

registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
});
loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
});
loginPopup.addEventListener('click', ()=>{
    wrapper.classList.add('active-popup');
});
closeIcon.addEventListener('click', ()=>{
    wrapper.classList.remove('active-popup');
});

//Patient Records
// === Add Popup Logic ===
const addPopup = document.querySelector('.addPop');
const patientDataForm = document.querySelector('.patient-data');

// Show the form when "Add" is clicked
addPopup?.addEventListener('click', (e) => {
    e.preventDefault();
    // Scroll to form
    patientDataForm.scrollIntoView({ behavior: 'smooth' });
    // Optional: Highlight it
    patientDataForm.style.boxShadow = '0 0 20px rgba(0,0,0,0.3)';
    setTimeout(() => {
        patientDataForm.style.boxShadow = ''; // reset after 1.5s
    }, 1500);
    // Focus on first input
    const firstInput = patientDataForm.querySelector('input');
    firstInput?.focus();
});

// === Basic Form Submit Validation ===
const form = document.querySelector('.patient-form');
form?.addEventListener('submit', (e) => {
    const requiredFields = form.querySelectorAll('input[required]');
    let allFilled = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            allFilled = false;
            field.style.borderColor = 'red';
        } else {
            field.style.borderColor = '';
        }
    });

    if (!allFilled) {
        e.preventDefault();
        alert('Please fill in all required fields.');
    }
});

// === Optional: Edit/Delete Logic Placeholder ===

const editBtn = document.querySelector('a[href="#"]:nth-of-type(2)');
const deleteBtn = document.querySelector('a[href="#"]:nth-of-type(3)');

editBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    alert("Edit functionality coming soon.");
});

deleteBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    const confirmDelete = confirm("Are you sure you want to delete this record?");
    if (confirmDelete) {
        alert("Deleted! (In future, this will remove the record)");
        // Implement backend call here
    }
});