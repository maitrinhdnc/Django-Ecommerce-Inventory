1. Install Virtual Environment and activate
2. Install Django: pip install django
3. Install project Ecommerce: django-admin startproject ecommerce .
4. Install pytest: 
    - pip install pytest-django
5. pip install pytest-factoryboy
    - integrate with pytest
    - generate data automatically for testing database 
6. pip install pytest-selenium
    - automate the evaluation of user interface
    - Example: test login process 
7. pip freeze > requirements.txt
8. Test Driven Development
    - Test methodology 
    - Build testcase first, write code second 
9. django-admin startapp dashboard
10. Dashboard folder -> Create folder tests -> __init__.py, test_selenium.py
11. Pytest focus file start with prefix 'test_' default but can set up at pytest.ini
12. Add conftest.py: help load all fixture, factory before running the test
13. Selenium require browser
14. Create admin info in database at fixture
15. pytest.ini -> tests | fi*xtures and selenium -> test_*.py
16. from django.contrib.auth.hashers import make_password
make_password('admin') => get hash string