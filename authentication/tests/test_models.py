from django import urls
import pytest

from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_create_user_without_username(client):
    username = ''
    email = 'mcdonaldotoyo44@gmail.com'
    password = 'MyTestAccount'
    user_model = get_user_model()
    
    with pytest.raises(ValueError) as exc_info:
        user_model.objects.create_user(username=username, email=email, password=password)
    assert 'Users must have a username!' == str(exc_info.value)
    

@pytest.mark.django_db
def test_create_user_without_email(client):
    username = 'McDonald'
    email = ''
    password = 'MyTestAccount'
    user_model = get_user_model()
    
    with pytest.raises(ValueError) as exc_info:
        user_model.objects.create_user(username=username, email=email, password=password)
    assert 'Users must have an email address!' == str(exc_info.value)
    

@pytest.mark.django_db
def test_create_superuser():
    username = 'McDonald'
    email = 'mcdonaldotoyo44@gmail.com'
    password = 'MyTestAccount'
    user_model = get_user_model()
    
    super_user = user_model.objects.create_superuser(username=username, email=email, password=password)
    assert super_user.is_admin == True
    assert super_user.is_staff == True
    assert super_user.is_superuser == True







