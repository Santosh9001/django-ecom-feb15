from django.urls import path

from .views import index,signup,handleSignup,handleLogin

urlpatterns = [
    path('index',index,name='index'),
    path('signup',signup,name='signup'),
    path('handleSignup',handleSignup,name='handleSignup'),
    path('handleLogin',handleLogin,name='handleLogin')
]