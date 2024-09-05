//Getting the Add button.
const addbutton = document.querySelector('.addbutton')

addbutton.addEventListener('click', function(){
    let taskform = document.querySelector('.formdetails');
    if(taskform.style.display == 'none' || taskform.style.display == ''){
        taskform.style.display = 'block'
    } else{
        taskform.style.display = 'none'
    }
    console.log('hey')
})

// Javascript dropdown bar bootstrap
const dropdownElementList = document.querySelectorAll('.dropdown-toggle');
const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl));