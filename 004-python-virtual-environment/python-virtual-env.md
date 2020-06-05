---
YamlDesc: CONTENT-ARTICLE
Title: python virtual environment
Keywords: python, virtual environment, example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: virtual-environment
---

# Python Virtual Environment
* Virtual Environment is a project setup mechanism, Where the modules required
  for that project are isolated from the system installed modules.
* It is good practice to have one new virtual environment for every Python 
  project, this helps in module dependencies isolation between projects.
* Steps to follow
  * Step 1. Install the virtualenev module using; `pip install virtualenv`
  * Step 2. Create a Folder where you want your virtual-environment and project to reside
    * `mkdir tinitiate`
  * Step 3. Navigate to that project-folder and create the virtual environment, 
    enter the following at the commandline 
    * `virtualenv my_project`  
  * Step 4. Activate the, go to the scripts folder and type to following at the commandline
    * `activate`
  * Step 5. Install other libraries, Go to the projects folder and install the 
    libraries requrired for the project, for example
    * `pip install flask`
