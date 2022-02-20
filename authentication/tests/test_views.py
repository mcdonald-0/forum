import pytest

from django.http import HttpResponse
from django import urls
from django.contrib.auth import get_user_model


@pytest.mark.parametrize('param', [
    ('authentication:signup'),
    ('authentication:signin'),
    ('authentication:logout'),
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('authentication:signup')
    response = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('authentication:signin')
    resp = client.post(login_url, data=user_data)
    assert resp.status_code == 200
  

@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse('authentication:logout')
    resp = client.get(logout_url)
    assert resp.status_code == 200








