from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('login/',views.login_view,name='login_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('')
]