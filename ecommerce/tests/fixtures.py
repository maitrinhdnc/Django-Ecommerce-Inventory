import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

@pytest.fixture
def create_admin_user(django_user_model):
    # django_user_model a tool of pytest allow select the user model
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("admin", "", "admin")

"""
* Because access DB default is not allowed so 
Django db blocker is object allow specific code path
to have access to the database

* If we want to create data in database, need to run dango_db_setup
"""
@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixture
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json") 