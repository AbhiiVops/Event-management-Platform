# Community Events Management Platform

Welcome to the Community Events Management Platform! This platform allows users to manage community events, including registration, creation, updating, deletion, and RSVP functionalities.

## Snapshot of the project:

<img src="images\dashboard.png" width="700" alt="Dashboard">

# Table of Contents
1. [Setup](#step-by-step-instructions-for-setting-up-the-project-locally)
2. [User Interaction Guide](#user-interaction-guide)
3. [Project Structure Overview](#project-structure-overview)
4. [Required Packages and versions](#required-packages-and-versions)
5. [Acknowledgements](#acknowledgments)

# Step-by-step instructions for setting up the project locally

Step 1:
    Clone This Project

        git clone https://github.com/AbhiiVops/Event-management-Platform.git

Step 2:
    Go to Project Directory

        cd django-event-management

Step 3:
    Create a Virtual Environment

        python3 -m venv env

Step 4:
    Activate Virtual Environment

      For Linux:
        source env/bin/activate

      For Windows:
        .\env\Scripts\activate  

Step 5:
    Install Requirements Package

        pip install -r requirements.txt

Step 6:
    Migrate Database

        python manage.py migrate

Step 7:
    Create Super User

        python manage.py createsuperuser

💡**Note:** *The default superuser with the username : `admin` and password : `admin` already exists. Create a new username and password.*

Step 8:
    Finally Run The Project

        python manage.py runserver


# User Interaction Guide

The following video shows how to perform various user interactions with the Event Management Platform:

Link to video: **https://youtu.be/Qc4RLWHdtgw**

1. **Registration**: Register for an account to access the platform's features.
2. **Login**: Log in to your account to manage events.
3. **Event Management**: Create, update, delete, and view events.
4. **RSVP**: RSVP to events and view RSVP status.

### Registration

- Navigate to the registration page.
- Fill in the required information and submit the form to get access to the platform.
- After successful registration, you will be redirected to the login page. You can now log in to your account

<img src="images\registeration.png" width="700" alt="Registration Page">

### Login

- Navigate to the login page.
- Enter your username and password and click on sign in.

<img src="images\login.png" width="700" alt="Login Page">

### Create Category

- In the sidebar, choose the "Create Category" option.
- Fill in the required information and submit the form.

<img src="images\Create_Event_Category.png" width="700" alt="Create-Event-Category Page">

### Create Event

- In the sidebar, choose the "Create Event" option.
- Fill in the required information and submit the form.

<img src="images\create_event.png" width="700" alt="create-event Page">

### Update/Delete Event

- In the sidebar, go to the "Events List" option.
- In the event list, in the action box select the "edit" option for edit and "delete" option for delete.

<img src="images\update_delete_event.png" width="700" alt="update_delete_event Page">

# Project Structure Overview

## App
- **events**: This app is responsible for managing events. It includes functionalities for creating, updating, deleting, and viewing events, as well as many other features.

## Models
- **Event**: Represents an event with attributes such as title, description, date, time, location, organizer details, and RSVP option.
- **UserProfile**: Extends the default User model to include additional profile information if needed.

## Views
- The views in the `events` app handle user requests related to event management, such as creating, updating, deleting, and viewing events.

## Templates
- HTML templates are used for rendering pages. These templates are located in the `templates` directory and include files for event listing, event detail, user authentication, etc.

## Static Files
- Static files such as CSS stylesheets, JavaScript files, and images are stored in the `static` directory. These files are used for styling and interactivity on the frontend.

## Configuration Files
- **settings.py**: Contains project-wide settings such as database configuration, static files configuration, and security settings.
- **urls.py**: Defines URL patterns and routes requests to appropriate views.

### In Short:

  - `community_events_management/`: Main project directory.
  - `events/`: Django app for managing events.
  - `templates/`: HTML templates.
  - `static/`: Static files (CSS, JavaScript, images).
  - `media/`: Uploaded files (event images, etc.).
  - `settings.py`: Django project settings.
  - `urls.py`: URL routing configuration.
  - `manage.py`: Django management script.



# Required Packages and Versions

The project requires the following Python packages and versions:

- asgiref==3.8.1
- asttokens==2.4.1
- attrs==23.2.0
- backcall==0.2.0
- beautifulsoup4==4.12.3
- bleach==6.1.0
- build==1.2.1
- CacheControl==0.14.0
- certifi==2024.2.2
- charset-normalizer==3.3.2
- cleo==2.1.0
- colorama==0.4.6
- crashtest==0.4.1
- crispy-bootstrap4==2024.1
- decorator==5.1.1
- defusedxml==0.7.1
- distlib==0.3.8
- Django==5.0.4
- django-betterforms==2.0.0
- django-ckeditor==6.7.1
- django-ckeditor-5==0.2.12
- django-crispy-forms==2.1
- django-js-asset==2.2.0
- django-mapbox-location-field==2.1.0
- docopt==0.6.2
- dulwich==0.21.7
- executing==2.0.1
- fastjsonschema==2.19.1
- filelock==3.13.3
- idna==3.6
- installer==0.7.0
- ipython==8.12.3
- jaraco.classes==3.4.0
- jedi==0.19.1
- Jinja2==3.1.3
- jsonschema==4.21.1
- jsonschema-specifications==2023.12.1
- jupyter_client==8.6.1
- jupyter_core==5.7.2
- jupyterlab_pygments==0.3.0
- keyring==24.3.1
- MarkupSafe==2.1.5
- matplotlib-inline==0.1.6
- mistune==3.0.2
- more-itertools==10.2.0
- msgpack==1.0.8
- nbclient==0.10.0
- nbconvert==7.16.3
- nbformat==5.10.4
- packaging==24.0
- pandocfilters==1.5.1
- parso==0.8.4
- pexpect==4.9.0
- pickleshare==0.7.5
- pillow==10.3.0
- pkginfo==1.10.0
- platformdirs==4.2.0
- poetry==1.8.2
- poetry-core==1.9.0
- poetry-plugin-export==1.7.1
- prompt-toolkit==3.0.43
- ptyprocess==0.7.0
- pure-eval==0.2.2
- Pygments==2.17.2
- pyproject_hooks==1.0.0
- python-dateutil==2.9.0.post0
- pywin32==306
- pywin32-ctypes==0.2.2
- pyzmq==25.1.2
- rapidfuzz==3.7.0
- referencing==0.34.0
- requests==2.31.0
- requests-toolbelt==1.0.0
- rpds-py==0.18.0
- setuptools==69.2.0
- shellingham==1.5.4
- six==1.16.0
- soupsieve==2.5
- sqlparse==0.4.4
- stack-data==0.6.3
- tinycss2==1.2.1
- tomlkit==0.12.4
- tornado==6.4
- traitlets==5.14.2
- trove-classifiers==2024.3.25
- tzdata==2024.1
- urllib3==2.2.1
- virtualenv==20.25.1
- wcwidth==0.2.13
- webencodings==0.5.1
- yarg==0.1.9

# Deployment on AWS EC2 instance 

<img src="images\deployment_on_ec2.png" width="700" alt="deployment_on_ec2">

# Acknowledgments

* The project is developed by **Abhishek Bhattacharjee**.
* This project covers the features of Event Management System.
* The project has been developed using monolithic approach.
* The project is developed using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* The project structure follows the Model-View-Template (MVT) pattern, which is similar to the Model-View-Controller (MVC) pattern.
* The project includes apps for managing events, user authentication, and user profiles.
* The project also includes models for events and user profiles, views for handling user requests, templates for rendering pages, and static files for styling and interactivity.
* The project is designed to be user-friendly and easy to navigate, with clear instructions for setting up the project locally and performing various user interactions.
* The project includes step-by-step instructions for setting up the project locally, as well as a user interaction guide for performing various tasks on the platform.
* The project structure overview provides an overview of the project's apps, models, views, templates, and static files.
* The required packages and versions are listed to ensure compatibility and functionality.
