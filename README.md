# Task Reminder
This is Task Reminder. It's designed to help users keeping track of importent things that need to get done.
user can create tasks, mark tasks as compleded, edit the tasks and delete tasks. You need to have an account to use the Task Reminder.
So user must create account by register and then have full access to the application.
This is a Full Stack project build with the django framework.

![alt text](assets/readme/Frist_pic.PNG)

## Task Reminder - Table Content

* [Planning and Design](#planning-and-design)
* [Agile methodology](#agile-methodology)
* [Wireframes](#wireframes )
* [Features](#features )
* [More Features](#more-features )
* [Libraries](#libraries )
* [Technical Stack](#technical-stack )



## Planning and Design

### User storys

#### Admin 
As a **Site Admin** I can **read, delete, update, and create tasks** so that **admin can fix problems**

* Be able to change the task, delete task, update task, create task.

#### Update or delete task 


As a **Site user** I can **Modify and delete tasks** so that **user can modify it as wanted**

* User can update the task.

* User can delete tasks.


#### Registration for using Task Reminder

As a **Site User** I can **Start using the Task Reminder** so that **can save the tasks in the list**

- User can register there own account.

- If user is logged in can use the task reminder to add task.

- Own site for log in.

#### Adding task

As a **Site User** I can **Add tasks to the task list** so that **Be able to remember the task needed to be done**

- User can add task.

- User get a response message when add task


## Agile methodology

Used an agile working method while working on this project. which worked, but first time apply this method on a project.
Its a good method to use to control that all of the things that need to be in the project actually is done.
You get to know where in the project you are.

#### 3 steps when using.

#### To Do
When the user story is created.
#### In Progress
When the user story is in progress to get done.
#### Done
When the user story is done.

<details>
<summary>Project Here</summary>
<br>
<img src="assets/readme/taskuser_Story.PNG">
</details>

#### User story information 
<details>
<summary>User story information</summary>
<br>
<img src="assets/readme/info_user_Story.PNG">
</details>

* With all the acceptance criterias that are needed.

### Diagram Models

<details>
<summary>Diagram models with </summary>
<br>
<img src="assets/readme/new_models.PNG">

* created with lucid.app
</details>

## Wireframes 

### display for mobile.
<details>
<summary>Homepage</summary>
<br>
<img src="assets/readme/mobile_index.PNG">
</details>

- index.html

<details>
<summary>Sign in page </summary>
<br>
<img src="assets/readme/login_mobil.PNG">
</details>

- sign in

<details>
<summary>Account registration </summary>
<br>
<img src="assets/readme/registration_mobil.PNG">
</details>

- Registration 

<details>
<summary>Contact page </summary>
<br>
<img src="assets/readme/contact_mobil.PNG">
</details>

- contact 

<details>
<summary>tasks </summary>
<br>
<img src="assets/readme/mobil_task_notopen.PNG">
</details>

- task page 


<details>
<summary>Task open </summary>
<br>
<img src="assets/readme/mopil_open_task.PNG">
</details>

- task page open

<details>
<summary>Add a task </summary>
<br>
<img src="assets/readme/added_tasks.PNG">
</details>

- add tasks

### Display for desktop

<details>
<summary>Homepage</summary>
<br>
<img src="assets/readme/desk_index.PNG">
</details>

- index.html

<details>
<summary>Sign in page </summary>
<br>
<img src="assets/readme/Sign_in_desk.PNG">
</details>

- sign in 

<details>
<summary>Sign up page</summary>
<br>
<img src="assets/readme/creat_acc_desk.PNG">
</details>

- sign up

<details>
<summary>Contact page</summary>
<br>
<img src="assets/readme/contact_desk.PNG">
</details>

- contact

<details>
<summary>Add task page</summary>
<br>
<img src="assets/readme/add_task_desctop.PNG">
</details>

- add task

<details>
<summary>Edit task page</summary>
<br>
<img src="assets/readme/edit_task_desk.PNG">
</details>

- edit 

<details>
<summary>Delete page </summary>
<br>
<img src="assets/readme/delete_task_desk.PNG">
</details>

- delete

<details>
<summary>Open task page</summary>
<br>
<img src="assets/readme/open_task_desktop.PNG">
</details>

- open task

<details>
<summary>Sign out page</summary>
<br>
<img src="assets/readme/sign_out.PNG">
</details>

- Sign out

## Features

### Navigationbar 

<details>
<summary>Navigation bar desktop</summary>
<br>
<img src="assets/readme/navbar_desktop.PNG">
</details>
<details>
<summary>Navigation bar mobil</summary>
<br>
<img src="assets/readme/nav_bar_mobil.PNG">
</details>

* Dropdown link to all pages if under 400px.(with icon from font awesome.)
* The navbar contains links to contact and sign up, login, and to the homepage.
* And changes if user is sign in to the website.(logout,contact, and home).
* responsive.

### Homepage

<details>
<summary>Homepage desktop</summary>
<br>
<img src="assets/readme/index_desktop.PNG">
</details>
<details>
<summary>Homepage mobil</summary>
<br>
<img src="assets/readme/homepage_mobil.PNG">
</details>

* Homepage shows user to register account to get access to the test reminder.
* show links to login
* shows link to register
* Responsive

### Tasks 

<details>
<summary>tasks desktop</summary>
<br>
<img src="assets/readme/logged_in_desktop.PNG">
</details>
<details>
<summary>tasks mobil</summary>
<br>
<img src="assets/readme/loged_in_user_mobil.PNG">
</details>

* Shows User where to add tasks.
* User can open there own tasks on the open button.
* Shows clear text where your new tasks are made.
* Responsive site.

### Edit tasks

<details>
<summary>Tasks edit desktop</summary>
<br>
<img src="assets/readme/edd_task_desktop.PNG">
</details>
<details>
<summary>Tasks edit mobil</summary>
<br>
<img src="assets/readme/create_task_mobil.PNG">
</details>

* User can add title,description and even time and date for tasks.

### Edit the made tasks

<details>
<summary>Tasks edit old task desktop</summary>
<br>
<img src="assets/readme/edit_task_desktop.PNG">
</details>
<details>
<summary>Tasks edit old task mobil</summary>
<br>
<img src="assets/readme/edit_task_mobil.PNG">
</details>

* Here user can Edit old tasks.
* user can choose the completed option in this edit here

### Delete page 

<details>
<summary>Delete page desktop</summary>
<br>
<img src="assets/readme/delete_task_desktop.PNG">
</details>
<details>
<summary>Delete page mobil</summary>
<br>
<img src="assets/readme/delete_mobil.PNG">
</details>

* User can choose to delete the task.
* User can choose to go back to the tasks.

### Sign out page 

<details>
<summary>sign out desktop</summary>
<br>
<img src="assets/readme/sign_out_desktop.PNG">
</details>
<details>
<summary>sign out mobil</summary>
<br>
<img src="assets/readme/sing_out_mobil.PNG">
</details>

* User can choose the option to sign out 
* User can go back to tasks.

### Sign in page

<details>
<summary>sign in desktop</summary>
<br>
<img src="assets/readme/login_desktop.PNG">
</details>
<details>
<summary>sign in mobil</summary>
<br>
<img src="assets/readme/login_mobil_app.PNG">
</details>

* User can choose the option to sign in. 
* User can go back to register.


### View task in list

<details>
<summary>view task desktop</summary>
<br>
<img src="assets/readme/view_task_desktop.PNG">
</details>
<details>
<summary>view task mobil</summary>
<br>
<img src="assets/readme/open_task_mobil.PNG">
</details>

* Here user can see the task that needs to be done
* Date and time.
* and options to delete or edit.

### Contact

<details>
<summary>Contact desktop</summary>
<br>
<img src="assets/readme/contact_desktop.PNG">
</details>
<details>
<summary>Contact mobil</summary>
<br>
<img src="assets/readme/contact_mobil_cool.PNG">
</details>

* User can send a contect for to Task reminder.

### Sign up for account

<details>
<summary>Register desktop</summary>
<br>
<img src="assets/readme/sign_up_desktop.PNG">
</details>
<details>
<summary>Register mobil</summary>
<br>
<img src="assets/readme/create_acc_mobil.PNG">
</details>

* User can create account for using the task reminder.
* or have the option to login if account already made.

### Searchbar

<details>
<summary>seachbar desktop</summary>
<br>
<img src="assets/readme/search_bar_desktop.PNG">
</details>
<details>
<summary>seachbar mobil</summary>
<br>
<img src="assets/readme/search_bar.PNG">
</details>

* User can search for task that exist in the list.
* error if no task exist of that name.
* need to fill in something in the search input.

### Footer

<details>
<summary>Footer desktop</summary>
<br>
<img src="assets/readme/footer_desk.PNG">
</details>
<details>
<summary>Footer mobil</summary>
<br>
<img src="assets/readme/footer_mobil.PNG">
</details>

* Footer contains copyright Task Remember


## More Features

* want to creat tasklist with categorys.
* when completed task goes into a done category.

## Libraries

* asgiref: Helps Django handle tasks in the background.
* dj-database-url: Makes it easier to set up the database.
* Django: The framework used to build the website.
* gunicorn: Runs the website on a server.
* psycopg2: Connects the website to a PostgreSQL database.
* sqlparse: Helps organize and format database queries.
* whitenoise: Helps the website with static files.

## Technical Stack
These are the things used for this project.

* Django - was used as framwork
* HTML -  Was used for front-end.
* CSS - Was used to style the site.
* Bootstrap - Used to style the website.
* Python - Made to create back-end.
* Javascript - for interactivity
* Gitpod - development environment
* Git - Version control system
* PostgreSQL - Database management system
* lucidchar - Creating my models Diagram.
* Heroku - deploying web applications

## Testing

### Lighthouse

## Validation
### W3C Testing
### CSS jigsaw
### jshint Javascript
### CI Python Linter

## Testing in django 

## Bugs

### unsolved bugs


## Deployment

### creating repository on github for project

### creating heroku application

### deploy to heroku 


## Credits

## Acknowledgements

