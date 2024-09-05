//Get the elements
const addbutton = document.getElementById('add-your-task')
addbutton.addEventListener('click', function(){
    console.log('hey')
})

// Javascript dropdown bar bootstrap
const dropdownElementList = document.querySelectorAll('.dropdown-toggle')
const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl))


