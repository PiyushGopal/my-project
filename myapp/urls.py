from django.urls import path 
from . import views
#helps us to add multiple urls to our list

urlpatterns = [
    #whenever an user goes through this link it sents an http request or 
    #a json response to the index function of views file or whateve function u have mentionend.
    path('', views.index, name='index'), # this is a single url, u can add multiple down here
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),# user authentication
    path('login',views.login, name='login'),
    path('logout', views.logout, name='logout'),
    #dynamic URL routing
    #it basically has a variable named 'pk' which is of string type
    path('post/<str:pk>', views.post, name='post'),
]