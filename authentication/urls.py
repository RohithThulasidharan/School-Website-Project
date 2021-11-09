from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name="home"),
    path('form', views.student_form, name='form'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('marks', views.student_marks_view, name='marks'),
    path('studentmarks', views.stumarksview, name='studentmarks'),
    path('Ranksearch', views.rankpageview, name='Ranksearch'),
    path('rankdisplay', csrf_exempt(views.rankdisplayview), name='rankdisplayview'),
]
