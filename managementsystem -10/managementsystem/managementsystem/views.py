from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import StudentUserForm
from .models import ElementaryStudent, MiddleStudent, HighStudent, HighSecondaryBioMathStudent, HighSecondaryComputerScienceStudent
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Assignments1


def home(request):
    return render(request, "managementsystem/index.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect("/")

def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid User Name or Password")
            return redirect("/login")
    return render(request, "managementsystem/login.html")

def register(request):
    form = StudentUserForm()

    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success. You can Login Now...!")
            return redirect('/login')

    return render(request, 'managementsystem/register.html', {'form': form})

# def assignment_list(request):
#     assignments = Assignments.objects.all()
#     return render(request, 'managementsystem/Assignments.html', {'assignments': assignments})



def home(request):
    # Obtain counts for each student category
    elementary_students_count = ElementaryStudent.objects.count()
    middle_students_count = MiddleStudent.objects.count()
    high_students_count = HighStudent.objects.count()
    bio_math_students_count = HighSecondaryBioMathStudent.objects.count()
    computer_science_students_count = HighSecondaryComputerScienceStudent.objects.count()

    # Obtain assignments
    assignments = Assignments1.objects.all()

    return render(request, 'managementsystem/index.html', {
        'elementary_students_count': elementary_students_count,
        'middle_students_count': middle_students_count,
        'high_students_count': high_students_count,
        'bio_math_students_count': bio_math_students_count,
        'computer_science_students_count': computer_science_students_count,
        'assignments': assignments,
    })



def assignment_list(request):
    assignments1 = Assignments1.objects.all()
    return render(request, 'managementsystem/Assignments.html', {'assignments1': assignments1})


def take_assignment(request, assignment_id):
    # Retrieve the assignment or return a 404 response if not found
    assignment1 = get_object_or_404(Assignments1, pk=assignment_id)

    # Assuming you have a related Quiz model and QuizQuestion model
    quiz_questions = assignment1.quiz.questions.all()

    return render(request, 'managementsystem/take_assignment.html', {'assignment1': assignment1, 'quiz_questions': quiz_questions})