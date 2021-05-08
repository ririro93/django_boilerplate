from django.urls import path, include

from .views import (
    profile,
    change_pw,
)

app_name = 'accounts'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('password/', change_pw, name='change_pw'),
]