//Getting the Add button.
const addbutton = document.querySelector('.addbutton');
// Function for addbutton in the front page for adding task.
addbutton.addEventListener('click', function(){
    let taskform = document.querySelector('.formdetails');
    if(taskform.style.display == 'none' || taskform.style.display == ''){
        taskform.style.display = 'block';
        taskform.style.paddingLeft = '5vh';
        addbutton.innerText = "X";
        addbutton.style.backgroundColor ='orange';
        addbutton.style.padding = '5px';
    } else{
        taskform.style.display = 'none';
        addbutton.innerText = "Add";
        addbutton.style.backgroundColor ='rgb(42, 156, 42)';
    }
})


//Getting the Add buttons to task list.
const addbuttontask = document.querySelectorAll('.task-buttons')
// Function for all the add buttons in the front page.
for (let i = 0; i < addbuttontask.length; i++){
    addbuttontask[i].addEventListener('click', function(){
        let taskinside = document.querySelectorAll('.task-details')[i];
      
            if(taskinside.style.display == 'none' || taskinside.style.display == ''){
                taskinside.style.display = 'block'
                taskinside.style.paddingLeft = '5vh'
                addbuttontask[i].innerText = "X";
                addbuttontask[i].style.backgroundColor ='orange';
                addbuttontask[i].style.padding = '5px';
        
            } else{
                taskinside.style.display = 'none'
                addbuttontask[i].innerText = "Add";
                addbuttontask[i].style.backgroundColor ='rgb(42, 156, 42)';
            }  
    })
}



// Javascript dropdown bar bootstrap
const dropdownElementList = document.querySelectorAll('.dropdown-toggle');
const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl));