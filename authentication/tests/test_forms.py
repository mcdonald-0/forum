from  django.db.utils import IntegrityError
from django.forms import ValidationError
from django.contrib.auth import authenticate, login
from django import urls
import pytest

from django.contrib.auth import get_user_model
from authentication.models import *
from authentication.forms import *

@pytest.mark.django_db
def test_create_user_with_existing_email(client, user_data, user_data_with_shared_email):
    user_model = get_user_model()
    signup_url = urls.reverse('authentication:signup') 
    user_1 = client.post(signup_url, user_data)
    user_2 = client.post(signup_url, user_data_with_shared_email)
    print(user_2.status_code)

    #! This is giving me a passed in pytest, Which is not correct. Adjust the test fuction so that it checks and render the forms.ValidationError and so it does'nt creates two users with the same email in the database!

    # with pytest.raises(ValidationError):
    #     check_email = user_model.objects.get(email=user_data_with_shared_email['email'])
    #         if check_email:
    #             user_model.objects.create(**user_data_with_shared_email)

   

    # if not authenticate(**user_data_with_shared_email):
    #     try:
    #         check_email = user_model.objects.get(email=user_data_with_shared_email['email'])
    #         if check_email:
    #             print('yes')
    #     except User.DoesNotExist:
    #         print('no')
    
    # try:
    #     user_model.objects.create(**user_data_with_shared_email)
    # except Exception as e:
    #     print(e)

    
        # if check_email:
        #     with pytest.raises(ValidationError) as exc_info:
        #         print(exc_info)
            #     check_email = user_model.objects.get(email=user_data_with_shared_email['email'])    
            # assert 'Users must have an email address!' == str(exc_info.value)
            

    # email = user_data_with_shared_email['email']
    # user = User.objects.get(email=email)
    # if user != None:
    #     print(f'There is {user}')
    # elif user.DoesNotExist:
    #     print(f'There is no {user}')


    


