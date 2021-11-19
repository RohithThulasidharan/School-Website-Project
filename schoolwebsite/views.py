import json
import re

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.views import View

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .models import Students, Exammarks
from .forms import StudentForm
from .serializers import ExammarksSerializer


# Create your views here.


# password policy validation view
class PasswordPolicyView(View):
    def post(self, request):
        data = json.loads(request.body)
        pwd = data['pass1']
        regex = "^(?=.{8,}$)(?=.*[a-zA-Z])(?=.*[0-9])(?=.*\W).*$"
        p = re.compile(regex)

        if len(pwd) < 8 or (not re.search(p, pwd)):
            return JsonResponse({'password_error': 'Password should contain a minimum of 8 characters,'
                                                   ' which has letters, numbers, and special characters'},
                                status=400)
        return JsonResponse({'password_valid': True})


# view for api functionality.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_exammarks_view(request, pk):
    try:
        exammarks = Exammarks.objects.get(pk=pk)
    except Exammarks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ExammarksSerializer(exammarks)
        return Response(serializer.data)


# view for student details input form
def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "schoolwebsite/studentregistrationform.html", {'form': form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student has been added")
        return redirect('/')


# Ajax page display
def rankpageview(request):
    return render(request, "schoolwebsite/ranksearchpage.html")


# Ajax rank display function
def rankdisplayview(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        pupils = Exammarks.objects.filter(classroomid__classroom_id=search_str).order_by('-total')[:5]
        data = pupils.values()  # returns a list

    return JsonResponse(list(data), safe=False)  # False lets us return a JSON response that is not a dictionary


# view function for webpage displaying marks
def student_marks_view(request):
    if 'q' in request.GET:
        ID = request.GET['q']  # the value entered in search bar is stored in q
        StudObj = Students.objects.filter(student_id__exact=ID)  # selecting student object based on student_id
        ExamObj = Exammarks.objects.filter(
            studentid__student_id=ID)  # selecting Exammarks object using the studentid foreign key

    else:
        ExamObj = Exammarks.objects.all()
        StudObj = Students.objects.all()
    return render(request, "schoolwebsite/studentmarks.html", {'exam': ExamObj, 'stud': StudObj})


# view for displaying student marks search page
def stumarksview(request):
    return render(request, 'schoolwebsite/markssearchpage.html')


# home page rendering view
def home(request):
    return render(request, "schoolwebsite/index.html")


# sign up registration view function
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try another username")
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signup')

        # if len(pass1) < 8:
        # raise ValidationError(('Password must be at least {0} characters '
        # 'long.').format(8))

        if len(pass1) < 8:
            messages.error(request, "Password must be a minimum of 10 characters")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

    return render(request, "schoolwebsite/signup.html")


# sign in authentication view function
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # return render(request, "schoolwebsite/index.html")
            return redirect('home')

        else:
            messages.error(request, "Bad credentials!")
            return redirect('home')

    return render(request, "schoolwebsite/signin.html", status=HTTP_200_OK)


# signout page
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')
