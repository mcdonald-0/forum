from unittest import TestCase
import pytest

from django.contrib.auth import get_user_model
# from django.test import TestCase

@pytest.mark.django_db
def test_create_user():
    username = ''
    email = 'mcdonaldotoyo44@gmail.com'
    password = 'MyTestAccount'
    user_model = get_user_model()
    
    TestCase.assertRaises(ValueError, user_model.objects.create_user(username=username, email=email, password=password))
    with TestCase.assertRaisesMessage(ValueError, 'Users must have a username!'):
        user_model.objects.create_user(username=username, email=email, password=password)
    
    
# ! Browse the internet for writing pytest that catches a value error because the one above just catches the error in the model






