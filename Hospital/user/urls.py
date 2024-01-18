from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('login/',views.login_view,name='login_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('all/hospitals/',views.view_all_hospitals,name='view_all_hospitals'),
    path('profile/<user_id>/',views.profile_view,name='profile_view'),
]