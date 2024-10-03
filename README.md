# Task Reminder
This is Task Reminder. It's designed to help users keeping track of important things that need to get done.
user can create tasks, mark tasks as completed, edit the tasks and delete tasks. You need to have an account to use the Task Reminder.
So user must create account by register and then have full access to the application.
This is a Full Stack project build with the django framework.
[Task Reminder Here](https://task-reminder-app-0c796f83bbb5.herokuapp.com/)
![responsive](<assets/readme/Screenshot 2024-10-03 at 19.09.04.png>)


## Task Reminder - Table Content

* [Planning and Design](#planning-and-design)
* [Agile methodology](#agile-methodology)
* [Wireframes](#wireframes )
* [Features](#features )
* [More Features](#more-features )
* [Libraries](#libraries )
* [Technical Stack](#technical-stack )
* [Testing](#testing)
* [Validation](#validation)
* [Testing in django](#testing-in-django)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)




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

- If user is sign in, user can add tasks.

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
<summary>Navigation bar mobile</summary>
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
<summary>Homepage mobile</summary>
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
<summary>tasks mobile</summary>
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
<summary>Tasks edit mobile</summary>
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
<summary>Tasks edit old task mobile</summary>
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
<summary>Delete page mobile</summary>
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
<summary>sign out mobile</summary>
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
<summary>sign in mobile</summary>
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
<summary>view task mobile</summary>
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
<summary>Contact mobile</summary>
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
<summary>Register mobile</summary>
<br>
<img src="assets/readme/create_acc_mobil.PNG">
</details>

* User can create account for using the task reminder.
* or have the option to login if account already made.

### Searchbar

<details>
<summary>searchbar desktop</summary>
<br>
<img src="assets/readme/search_bar_desktop.PNG">
</details>
<details>
<summary>searchbar mobile</summary>
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
<summary>Footer mobile</summary>
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

#### Desktop Lighthouse
<details>
<summary>Desktop results</summary>
<br>
<img src="assets/readme/desktop_ligthhouse.PNG">
</details>

#### Mobile Lighthouse
<details>
<summary>Mobile results</summary>
<br>
<img src="assets/readme/Ligthhouse_mobile.PNG">
</details>




## Validation

### W3C Testing
<details>
<summary>Index tested</summary>
<br>
<img src="assets/readme/index_no_warning.PNG">
</details>

<details>
<summary>Contact tested</summary>
<br>
<img src="assets/readme/contect_no_erro.PNG">
</details>

<details>
<summary>sign in tested</summary>
<br>
<img src="assets/readme/login_no_error.PNG">
</details>

<details>
<summary>sign up tested</summary>
<br>
<img src="">
</details>

<details>
<summary>Sign out tested</summary>
<br>
<img src="">
</details>

<details>
<summary>tasks tested</summary>
<br>
<img src="">
</details>

<details>
<summary>edit tested</summary>
<br>
<img src="">
</details>

<details>
<summary>delete tested</summary>
<br>
<img src="">
</details>

<details>
<summary>success page tested tested</summary>
<br>
<img src="">
</details>


### CSS jigsaw

<details>
<summary>CSS Test</summary>
<br>
<img src="assets/readme/css_ok.PNG">
</details>


### jshint Javascript

<details>
<summary>Jshint javascript </summary>
<br>
<img src="assets/readme/jshint_javascript.PNG">
</details>

* Jshint shows one warning that function may lead to confusing semantics, since its inside the loops.


### CI Python Linter

<details>
<summary>Views test</summary>
<br>
<img src="assets/readme/views_cleeen.PNG">
</details>

<details>
<summary>Models test</summary>
<br>
<img src="assets/readme/models_py.PNG">
</details>

<details>
<summary>urls test</summary>
<br>
<img src="assets/readme/urls_right.PNG">
</details>

<details>
<summary>forms test</summary>
<br>
<img src="assets/readme/formmmmmmss.PNG">
</details>



## Testing in django 

### views

| Status | **Sign Out - Redirect to Homepage** |
|:------:|:-----------------------------------
| &check; | When the user logs out, they are redirected to the homepage (status code 302). 

| Status | **Sign In - Valid Sign In** |
|:------:|:----------------------------
| &check; | When the user enters the correct username and password, they are taken to the task creation page (status code 302). 

### Models 


| Status | **Contact Form - Valid Data** |
|:------:|:-------------------------------
| &check; | When the user submits the contact form with valid data, it gets saved. 

### Forms

### Post User First Test

| Status | **Post User First - Valid Data** 
|:------:|:----------------------------------
| &check; | When the user submits the form with all required fields completed, the form is valid.



## Bugs
#### No bugs found.

### unsolved bugs
#### None.


## Deployment

### creating repository on github for project

* Sign in to GitHub then go to use https://github.com/Code-Institute-Org/ci-full-template.
* click to "use this template" and Create a new repository.
* create a repository with name in the Repository name
* then create Repository 

### creating heroku application
* Sign in to heroku.
* In the landing page press the dropdown and click on create app.
* give the application a name, and choose the location(Europe).

### deploy to heroku 
* Go to the settings tab when clicked into your new app.
* go to the config vars section.
* add a key of DISABLE_COLLECTSTATIC and value of 1,so heroku dont upload staticfiles during build.
* install gunicorn in the command.
* install the requirements.txt.
* Create a Procfile.
* and put in '.herokuapp.com' to ALLOWED_HOSTS.
* In heroku go to deploy scroll down to "Manual deploy" and press the button Deploy Branch.

## Credits
### Help from these websites
https://www.pythontutorial.net/django-tutorial/django-updateview/ 
https://dev.to/nuh/django-loginview-and-flash-messages-4k9k
https://www.w3schools.com/
https://getbootstrap.com/docs/5.3/components/alerts/#examples
https://docs.djangoproject.com/en/5.1/
https://www.youtube.com/watch?v=WuyKxdLcw3w&t=238s
https://stackoverflow.com/questions/1042900/django-unit-testing-with-date-time-based-objects
https://docs.djangoproject.com/en/5.1/topics/auth/default/#django.contrib.auth.models.User
https://medium.com/@buczynski.rafal/navigation-through-django-views-testing-907091f97638
https://dev.to/ifihan/testing-in-django-26e5
https://medium.com/@buczynski.rafal/navigation-through-django-views-testing-907091f97638
https://fontawesome.com/
https://getbootstrap.com/
https://balsamiq.com/
https://coolors.co/ for the colors in the website.

## Acknowledgements
* I would like to thank my mentor, Spence for help with guidance with my project.
