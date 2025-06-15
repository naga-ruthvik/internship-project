from django.urls import path
from . import views

urlpatterns=[
    path('',views.signup,name='signup'),
    path('login/',views.signin,name='signin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout/',views.signout,name='logout')

]