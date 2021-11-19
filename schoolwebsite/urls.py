from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('studentregistration', views.student_form, name='form'),  # student registration page
    path('signup', views.signup, name='signup'),  # signup page
    path('signin', views.signin, name='signin'),  # sign in page
    path('signout', views.signout, name='signout'),  # sign out view
    path('marks', views.student_marks_view, name='marks'),  # student marks display page
    path('markssearch', views.stumarksview, name='studentmarks'),  # student marks search page
    path('ranksearch', views.rankpageview, name='Ranksearch'),  # rank search page
    path('rankdisplay', csrf_exempt(views.rankdisplayview), name='rankdisplayview'),  # rank display AJAX view

    # api authenticated view for student marks display
    url(r'^api/authentication/(?P<pk>[0-9]+)$', views.api_exammarks_view),

    # API endpoint for user token
    path('api-token-auth/', obtain_auth_token, name= 'api_auth_token'),

    # password policy view
    path('password-policy', csrf_exempt(views.PasswordPolicyView.as_view()), name='password-policy'),
]
