from django.forms import ValidationError
from django.contrib.auth import authenticate, login
import pytest

from django.contrib.auth import get_user_model
from authentication.models import *

@pytest.mark.django_db
def test_create_user_with_existing_email(request, user_data, user_data_with_shared_email):
    user_model = get_user_model()
    user_1 = user_model.objects.create(**user_data)
    user_login = authenticate(**user_data_with_shared_email)    
    if not user_login:
        
        User.objects.get(email=user_data_with_shared_email['email'])

        with pytest.raises(ValidationError) as exc_info:
            email = user_data_with_shared_email['email']
            user = User.objects.get(email=email)
            if user != None:
                assert f'Incorrect password for email "{email}"😓' == str(exc_info.value)
            elif user.DoesNotExist:
                assert 'You do not have an account yet😕, try creating one🙂!' == str(exc_info.value)


    


