
# Psychiatric Prescribing Guide: Developer Support
Webapp to automate the Prescribing Pocket Guide 2012 process
## 1. Obtain the source code

---
The latest code for this web application is located at 
  [https://github.com/Brick7Face/psychiatric-guide-app](https://github.com/Brick7Face/psychiatric-guide-app).


### 1.1 Source code for latest stable/released version

The source code for the latest releases can be found on the opening page of the website above on the master branch. The releases themselves can be found on the releases tab.


### 1.2 Source code for development

The development source code is found on the branch "development" in the branches tab. 


## 2. Directory Layout

---

The directory layout of the application consists primarily of the main directory "/psychiatric-guide-app", two subdirectories ("/application" and "/psychiatric_guide_app"), and a template directory("/application/templates/application").  

The directory at "/psychiatric_guide_app/psychiatric_guide_app" contains files for settings, url routes, and wsgi for the overall project.  The directory at "/psychiatric_guide_app/application" contains files to render requests and control urls at links within /application and tests.

To access, edit, and view html source files, locate the directory at /application/templates/application. Finally, this documentation is accessible from a link on the website. For more questions, please email [njtranel@gmail.com](mailto:njtranel@gmail.com).   


## 3. Using the software

---

### 3.1 How to compile/ build:

Since our software is a web application, there is not exactly a way to compile it explicitly. However, since it needs to be publicly hosted, to see changes in development, one can run from the command line the command **python manage.py runserver** in the same directory as the manage.py file to host it locally. One certain Linux operating systems, the command should instead be **python3 manage.py runserver**. This will host the application on local host at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). 


### 3.2 How to test:

All that needs to be done to run tests are to be in the same directory as the test.py file and run it from the command line. We also setup these tests to run automatically in a script, which is detailed below. Alternatively, tests can be run from the command line in the same directory as the .travis.yml file with the command **python -m unittest discover**.


#### 3.2.1 How to set up an automated weekly (or more frequent) build and test

For automated testing, our application uses the Travis CI tool. This tool is openly available at [https://travis-ci.org/](https://travis-ci.org/). To use it in a project, one simply has to sign in with their Github account and the tool will automatically detect projects from that account. A switch can then be toggled next to the project in question to enable the tool to watch that project. Within the top directory of that project, the .travis.yml file specifies how to automatically run tests daily and whenever a new commit is pushed to Github. When tests fail, the contributors to the project are emailed, and the person who pushes the commit always gets emailed either way. These automatic tests can be configured to run daily, weekly, or monthly from the Travis CI website. Our tests run daily. The results of the test suite are displayed beside the commit on Github, though more details are available from the Travis CI website.

Our .travis.yml file simply specifies the language to use, the version of that language makes sure that the correct dependencies are installed based on the included requirements.txt file, and then runs a script where our unit tests are located. 


## 4. How to release a new version



---


Our application is hosted on Google App Engine. App Engine is a fully managed serverless application platform which handles the majority of the management required to host a web application.


### 4.1 Updating revision numbers

The application should be updated in two places. First, update the version number in the **settings.py** file. Secondly, **create a new release on github** with the same version number that was updated in settings.py.


### 4.2 How to make a package that the user uses to obtain product

Use the command **python manage.py collectstatic **to create a static directory which contains the necessary files for hosting the application on App Engine.


### 4.2 Make new version public

To make the new application version available to the public you will first need the credentials for the Google Cloud account. Using these credentials, run **gcloud app deploy** in order to deploy the application to 
  
  https://psychiatric-guide.appspot.com/

