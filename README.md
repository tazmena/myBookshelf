# myBookshelf

## Installation Instructions
You may need to install the following:
 - https://docs.conda.io/en/latest/miniconda.html (Miniconda, for the virtual environment)
 - Create a conda environment: conda create --name myBookshelf python=3.9
 - Activate the environment: conda activate myBookshelf
 - cd into outer myBookshelf folder
 - python --version (ensure python version is 3.9)
 - pip install django
 - pip install --upgrade pip
 - pip install -U scikit-learn
 - pip install numpy
 - pip install pandas (or conda install pandas)
 - pip install django-cors-headers
 
 In another terminal, cd to outer myBookshelf folder, and frontend
 - Activate the conda environment created above: conda activate myBookshelf
 - npm i @fortawesome/fontawesome-free
 - npm install vue-router@4
 - npm install
 
 Once all installations complete, you can run by:
 
 In a first terminal:
 - cd into outer myBookshelf folder
 - activate the environment: conda activate myBookshelf
 - run the server: python manage.py runserver
 
 In another terminal window:
 - cd into outer myBookshelf folder
 - cd into frontend
 - activate the environment: conda activate myBookshelf
 - run the server: npm run dev
 
 To get to the login page, go to http://localhost:8000/bookapp/
 Ensure that this is local host and not numbers such as 127...
 Please note that the recommendations take a while to load.
 
 In case it is needed, here are the admin login details:
 username: admin
 password: admin
 
 And another account user for testing:
 username: tazmena31
 password: password123
