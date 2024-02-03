from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import StudentUserForm
from .models import ElementaryStudent, MiddleStudent, HighStudent, HighSecondaryBioMathStudent, HighSecondaryComputerScienceStudent
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Assignment, QuizSubmission
from .forms import QuizSubmissionForm
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

def assignment_list(request):
    assignments = Assignments.objects.all()
    return render(request, 'managementsystem/Assignments.html', {'assignments': assignments})



def home(request):
    # Obtain counts for each student category
    elementary_students_count = ElementaryStudent.objects.count()
    middle_students_count = MiddleStudent.objects.count()
    high_students_count = HighStudent.objects.count()
    bio_math_students_count = HighSecondaryBioMathStudent.objects.count()
    computer_science_students_count = HighSecondaryComputerScienceStudent.objects.count()

    # Obtain assignments
    assignments = Assignments.objects.all()

    return render(request, 'managementsystem/index.html', {
        'elementary_students_count': elementary_students_count,
        'middle_students_count': middle_students_count,
        'high_students_count': high_students_count,
        'bio_math_students_count': bio_math_students_count,
        'computer_science_students_count': computer_science_students_count,
        'assignments': assignments,
    })

def assignment_details(request, assignment_id):
    assignment = get_object_or_404(Assignments, id=assignment_id)
    questions = json.loads(assignment.questions)
    # Add any additional logic or context data you need
    return render(request, 'managementsystem/assignment_details.html', {'assignment': assignment, 'questions': questions})

@login_required
def submit_quiz(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    # Check if the user has already submitted the quiz for this assignment
    existing_submission = QuizSubmission.objects.filter(assignment=assignment, user=request.user).exists()
    if existing_submission:
        messages.error(request, "You have already submitted this quiz.")
        return redirect('assignment_details', assignment_id=assignment.id)

    if request.method == 'POST':
        form = QuizSubmissionForm(request.POST)
        if form.is_valid():
            # Save the quiz submission
            submission = form.save(commit=False)
            submission.user = request.user
            submission.assignment = assignment
            submission.save()

            messages.success(request, "Quiz submitted successfully.")
            return redirect('assignment_details', assignment_id=assignment.id)
    else:
        form = QuizSubmissionForm()

    return render(request, 'managementsystem/quiz_submission.html', {'form': form, 'assignment': assignment})