import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import FinalExamMarks, Students, Exammarks, Classrooms
from .forms import StudentForm
from .serializers import ExammarksSerializer


# Create your views here.

# view for student details input form
def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "authentication/student_form.html", {'form': form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student has been added")
        return redirect('/')

# Ajax page display
def rankpageview(request):
    return render(request, "authentication/Ranksearch.html")

# Ajax rank display function
def rankdisplayview(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        pupils = Exammarks.objects.filter(classroomid__classroom_id=search_str).order_by('-total')[:5]

        Exammarks_serializer = ExammarksSerializer(pupils, many=True)

        #data = Exammarks_serializer.values()

        data = pupils.values() # returns a list

    return JsonResponse(list(data), safe=False) # False lets us return a JSON response that is not a dictionary

# view function for webpage displaying marks
def student_marks_view(request):
    if 'q' in request.GET:
        q = request.GET['q']  # the value entered in search bar is stored in q
        spud = Students.objects.filter(student_id__exact=q)  # selecting student object based on student_id
        stud = Exammarks.objects.filter(studentid__student_id=q)  # selecting Exammarks object using the studentid foreign key

    else:
        stud = FinalExamMarks.objects.all()
        spud = Students.objects.all()
    return render(request, "authentication/marks1.html", {'stu': stud, 'spu': spud})

# view for displaying student marks search page
def stumarksview(request):
    return render(request, 'authentication/studentmarks.html')


# home page rendering view
def home(request):
    return render(request, "authentication/index.html")

# sign up registration view function
def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try another username")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

    return render(request, "authentication/signup.html")

# sign in authentication view function
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad credentials!")
            return redirect('home')
    return render(request, "authentication/signin.html")

# signout page
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')
