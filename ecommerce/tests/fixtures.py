import pytest

@pytest.fixture
def create_admin_user(django_user_model):
    # django_user_model a tool of pytest allow select the user model
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser("admin", "", "admin")