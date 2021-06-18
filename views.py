from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib import messages

#views
from django.views import View

#models
from django.contrib.auth.models import User
from users.models import Student, Teacher, Subject

def login_view(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('landing')
        else:
            try:
                user = User.objects.get(username=username)
                return render(request, 'users/login.html', {'Error': 'Invalid password'})
            except:
                return render(request, 'users/login.html', {'Error': 'Invalid username and password'})

    return render(request, 'users/login.html')

def signup(request):

    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['confirmpassword']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password do not match'})

        try:
            if User.objects.get(email= request.POST['email']):
                return render(request, 'users/signup.html', {'error' : ' Email already taken'})
        except :
            pass

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error' : 'Username already taken '})

        user.first_name = request.POST['name']
        user.last_name= request.POST['lastname']
        user.email= request.POST['email']
        user.save()
        type_of_user = request.POST['type']

        if type_of_user == 'teacher':
            profile = Teacher(user=user)
        else:
            profile = Student(user=user)

        profile.save()

        messages.success(request, "the account was created succesfully")
        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def landing(request):
    return render(request, 'landing.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def update_teacher_profile(request):
    teacher = request.user.teacher
    if request.method == 'POST':
        teacher.title = request.POST['title']
        teacher.save()
        return render(request, 'landing.html', {'user', 'teacher'})
    return render(request, 'users/update_teacher_profile.html')

@login_required
def update_student_profile(request):

    student = request.user.student
    if request.method == 'POST':
        subjects = Subject.objects.all()

        student.student_number= request.POST['student_number']
        student.group= request.POST['group']
        student.career = request.POST['career']

        for subj in subjects:
            try:
                _subject = Subject.objects.get(short_name=request.POST[f'{subj}'])

                student.subject.add(_subject)
            except:
                pass
        student.save()
        return redirect('landing')

    subjects = Subject.objects.all()
    careers = Student.CAREERS
    career_option = []

    for career in careers:
        career_option.append(career[0])
    return render(request, 'users/update_student_profile.html', {"subjects":subjects, "career_option":career_option})