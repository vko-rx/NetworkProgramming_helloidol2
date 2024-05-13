# helloidol2 
---
1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > settings... > Language & Frameworks > Django
        [v] Enable Django Support
   4. Run > Edit configurations... > + > Django Server > Name: runserver
   5. VCS > Enable Version Control Intergration... > git > ok
2. startapp mood
   1. python manage.py startapp mood
   2. 'mood', in INSTALLED_APPS in settings.py
3. mood/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
      2. python manage.py makemigrations mood
      3. python manage.py migrate mood